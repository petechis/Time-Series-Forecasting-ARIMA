
# 🚗 Car Dealer Sales Forecasting with ARIMA  
### AI-powered decision support for automotive distributors

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)
![Statsmodels](https://img.shields.io/badge/Statsmodels-ARIMA-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Time Series](https://img.shields.io/badge/ML-Time%20Series-success)
![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-brightgreen)

[English](README.md) | [German](./translations/DE/README.md)

## ✨ Business Problem

A **car distributor** works with multiple dealers and wants to know:

✔ How many vehicles each dealer is likely to sell  
✔ Which brand will grow or decline  
✔ What revenue may look like in the coming months  
✔ Where to optimize stock, incentives, and marketing  

Instead of guessing → we **forecast**.

---

## 🧠 Solution

This application uses **ARIMA time series forecasting** to learn from historical sales and predict the **next 3 months** for any:

- 🚘 Car Model  
- 🤝 Seller / Dealer  

The result is delivered in:

📋 **tabular predictions**  
📈 **visual trend charts**  
📝 **automatic business storytelling**

---

## 🖥 Application Preview

![Business Meeting](img/business_advisor_meeting.png)

---

## ⚙️ How It Works (Simple & Powerful)

![Landing Page](img/Landing_page.png)

### **Input**
User selects:
- Product → *Mercedes-Benz, Volkswagen, Audi, Porsche, BMW*
- Seller → *George, Prince, Robin*

### **Process**
1. Filter historical data  
2. Build time series  
3. Train **ARIMA(2,1,1)**  
4. Forecast next 3 months  
5. Format results for business users  

### **Output**
✅ Car Sales Predictions per Seller  
✅ Sales Prediction Chart  
✅ Written interpretation & insights  

---

## 🔮 Example Outcome

After clicking **Make Prediction**, the distributor instantly sees:

| Date | Product | Seller | Forecast |
|------|---------|--------|----------|
| 09-24 | Porsche | Robin | 35 |
| 10-24 | Porsche | Robin | 28 |
| 11-24 | Porsche | Robin | 33 |

Plus a clear visual line chart.

This enables faster:

- inventory planning  
- bonus steering  
- performance evaluation  
- campaign timing  

---

## 🏗 Architecture Overview

```

CSV Historical Data
↓
Filtering (Product + Seller)
↓
Time Series Creation
↓
ARIMA Model Training
↓
3-Month Forecast
↓
Table + Chart + Storytelling

```

---

## 📂 Project Structure

```

car-part-sales.csv        # historical dataset
img/                      # UI images
app.py                    # Streamlit application
formatted_characters.py   # styling & storytelling helpers
requirements.txt          # dependencies
README.md

````

---

## 🧩 Technologies Used

| Area | Stack |
|------|------|
Data Processing | Pandas |
Forecasting | Statsmodels ARIMA |
Date Handling | dateutil |
Frontend | Streamlit |
Visualization | Streamlit Charts |

---

## 🔁 Possible Future Upgrades (Recruiters love this part)

⭐ Prophet / LSTM comparison  
⭐ Confidence intervals  
⭐ Revenue = Sales × Price  
⭐ Dealer ranking  
⭐ What-if simulations  
⭐ API deployment  
⭐ Live database instead of CSV  
⭐ Auto retraining  
⭐ Downloadable reports  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
````

---

## 🎯 What This Project Demonstrates

✔ Machine Learning in real business context

✔ Converting raw data → management insight

✔ Building usable analytics apps

✔ Time series modelling

✔ Stakeholder-friendly visualization

✔ Analytical storytelling

✔ Production thinking

---

## 👤 Author

**Pete Chisamba**

Data & AI Enthusiast focused on decision intelligence, automation, and business value.

---
