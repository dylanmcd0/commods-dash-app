# Commodity Analysis Dashboard

## 📌 Project Overview
A random project for me to get better at tracking, analyzing, and understanding **oil & gas markets**.

As well as (hopefully at some point) how to convert data into insights, and insights into positions.

### **🔹 Features (maybe one day)**
- 📈 **Price Forecasting** using ML (ARIMA, LSTM, etc.)
- 📊 **Fundamental Analysis** of oil inventories, macroeconomic indicators, and supply-demand factors
- 📉 **Technical Analysis** with interactive charts (RSI, MACD, Bollinger Bands)
- 📰 **News & Sentiment Analysis** via web scraping and NLP
- 📡 **Live (free) Data Integration** from Yahoo Finance, EIA, and FRED

---
## If Anyone Cares to Run Locally
### Clone the Repo
```bash
git clone https://github.com/yourusername/commods-dash-app.git
cd commods-dash-app
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Dash App
```bash
python src/app.py
```
The app will be accessible at: **http://127.0.0.1:8050/**

To stop the running app, press:
```
CTRL + C
```

---
## 📁 Goal Project Structure
```
commods-dash-app/
│── data/                  # Raw & processed datasets (maybe a db)
│── models/                # ML models for price prediction (maybe a scheduler / db)
│── notebooks/             # Jupyter notebooks for research
│── src/                   # Dash app source code
│   ├── app.py             # Main entry point
│   ├── layout.py          # Layout components
│   ├── callbacks.py       # Callback logic
│   ├── tabs/              # Modular tab structure
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---
## 🌍 Deployment
The idea is to eventually get this app deployed using **Heroku, AWS, or Google Cloud** (whatever is cheapest). Deployment information will be added whenever that happens.

---
## 👤 Author
**Dylan McDonald**  
📧 Contact: [dylmcdona@icloud.com](mailto:dylmcdona@icloud.com)  
🔗 LinkedIn: [linkedin.com/in/dylan-mcdonald-91b8641aa](https://linkedin.com/in/dylan-mcdonald-91b8641aa)

---
## 🛠️ To-Do List
✅ Basic Dash app setup  
🔜 Implement machine learning models for price forecasting  
🔜 Integrate real-time data sources  
🔜 Deploy the application  

