# Commodity Analysis Dashboard

## 📌 Project Overview
A bit of a random project designed to track and analyze **oil & gas markets**.

### **🔹 Features (maybe)**
- 📈 **Price Forecasting** using machine learning (e.g., ARIMA, XGBoost, LSTM)
- 📊 **Fundamental Analysis** of oil inventories, macroeconomic indicators, and supply-demand factors
- 📉 **Technical Analysis** with interactive charts (RSI, MACD, Bollinger Bands)
- 📰 **News & Sentiment Analysis** via web scraping and NLP
- 📡 **Live Data Integration** from Yahoo Finance, EIA, and FRED

---
## How to Get Started
### **1️ Clone the Repository**
```bash
git clone https://github.com/yourusername/commods-dash-app.git
cd commods-dash-app
```

### **2️ Set Up a Virtual Environment**
```bash
python -m venv venv
# Activate venv:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### **3️ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️ Run the Dash App**
```bash
python src/app.py
```
📍 The app will be accessible at: **http://127.0.0.1:8050/**

### **5️ Stop the Dash App**
To stop the running app, press:
```
CTRL + C
```

---
## 📁 Project Structure
```
commods-dash-app/
│── data/                  # Raw & processed datasets
│── models/                # ML models for price prediction
│── notebooks/             # Jupyter notebooks for research
│── src/                   # Dash app source code
│   ├── app.py             # Main entry point
│   ├── layout.py          # Layout components
│   ├── callbacks.py       # Callback logic
│   ├── tabs/              # Modular tab structure
│── static/                # CSS & UI assets
│── tests/                 # Unit tests
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---
## 🌍 Deployment
This app can be deployed using **Heroku, AWS, or Google Cloud**. Deployment instructions will be added soon (haven't done this yet).

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

