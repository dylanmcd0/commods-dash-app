import pandas as pd
import numpy as np
import yfinance as yf
import os
import requests
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create necessary directories
DATA_DIR = "data"
MODEL_OUTPUT_DIR = "model_outputs"
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_OUTPUT_DIR, exist_ok=True)


# Fetch data function
def fetch_data():
    ticker = "CL=F"  # WTI Crude Oil Futures
    df = yf.download(ticker, start="2000-01-01", end="2025-01-01")
    df = df[["Close"]].rename(columns={"Close": "WTI_Price"})

    # Fetch U.S. Dollar Index (DXY)
    dxy = yf.download("DX-Y.NYB", start="2000-01-01", end="2025-01-01")[["Close"]]
    dxy.rename(columns={"Close": "DXY"}, inplace=True)

    # Fetch Crude Oil Inventories (EIA)
    eia_api_key = os.getenv("EIA_API_KEY")
    eia_url = (
        f"https://api.eia.gov/series/?api_key={eia_api_key}&series_id=PET.WCESTUS1.W"
    )
    response = requests.get(eia_url).json()

    inventory_data = response["series"][0]["data"]  # Extract inventory data
    inventory_df = pd.DataFrame(inventory_data, columns=["Date", "Crude_Inventory"])
    inventory_df["Date"] = pd.to_datetime(inventory_df["Date"])
    inventory_df.set_index("Date", inplace=True)

    # Merge datasets
    df.index.name = "Date"
    merged_df = df.join([dxy, inventory_df], how="left")
    merged_df.to_csv(os.path.join(DATA_DIR, "oil_data_with_features.csv"))

    return merged_df


# Preprocess data
def preprocess_data():
    df = pd.read_csv(
        os.path.join(DATA_DIR, "oil_data_with_features.csv"),
        parse_dates=["Date"],
        index_col="Date",
    )
    df.fillna(method="ffill", inplace=True)
    df = df.asfreq("B")  # Ensure business day frequency
    return df


# Train ARIMA model
def train_arima_model(df):
    y = df["WTI_Price"]
    X = df[["DXY", "Crude_Inventory"]]
    y_diff = y.diff().dropna()
    X = X.loc[y_diff.index]

    model = auto_arima(
        y_diff,
        exogenous=X,
        seasonal=False,
        stepwise=True,
        trace=True,
        suppress_warnings=True,
    )
    best_order = model.order
    print(f"Best ARIMA Order: {best_order}")

    arima_model = ARIMA(y, order=best_order, exog=X).fit()
    arima_model.save(os.path.join(MODEL_OUTPUT_DIR, "arima_model.pkl"))
    return arima_model


# Forecast future prices
def forecast_prices(model, df, steps=30):
    X_future = df[["DXY", "Crude_Inventory"]].iloc[-steps:]
    forecast = model.forecast(steps=steps, exog=X_future)
    forecast_dates = pd.date_range(df.index[-1], periods=steps + 1, freq="B")[1:]
    forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecasted_Price": forecast})
    forecast_df.set_index("Date", inplace=True)
    forecast_df.to_csv(os.path.join(MODEL_OUTPUT_DIR, "forecast_prices.csv"))
    return forecast_df


# Run the pipeline
if __name__ == "__main__":
    print("Fetching data...")
    fetch_data()

    print("Preprocessing data...")
    processed_data = preprocess_data()

    print("Training ARIMA model...")
    arima_model = train_arima_model(processed_data)

    print("Forecasting future prices...")
    forecast_data = forecast_prices(arima_model, processed_data)
    print(forecast_data.head())
