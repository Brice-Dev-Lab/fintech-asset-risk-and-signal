# ⚙️ Feature Engineering

## 🧠 Goal

Create meaningful signals from price data.

---

## 🔹 Returns (uses shift)

    returns = prices / prices.shift(1) - 1

---

## 🔹 Volatility (risk proxy)

    vol = returns.rolling(20).std()

---

## 🔹 Momentum

    momentum = prices / prices.rolling(20).mean() - 1

---

## 🧭 Result

Three key datasets:

- returns
- volatility
- momentum

---

## 💡 Insight

These are foundational features for risk modeling.