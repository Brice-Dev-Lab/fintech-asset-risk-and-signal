# 📥 Data Ingestion

## 🧠 Goal

Retrieve real financial data using an API.

---

## 🔧 Example (yfinance)

    import yfinance as yf

    tickers = ['SPY','QQQ','TLT','GLD','^VIX']
    data = yf.download(tickers, start='2020-01-01', end='2024-01-01')

---

## ⚠️ Notes

- Data is returned with a MultiIndex (columns)
- Focus on adjusted close prices

---

## 🔄 Extract Prices

    prices = data['Adj Close']

---

## 🧭 Result

| Date | SPY | QQQ | TLT | GLD | VIX |

A clean, time-indexed dataset