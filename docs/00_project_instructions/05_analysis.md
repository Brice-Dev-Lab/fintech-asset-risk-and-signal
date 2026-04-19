# 📊 Analysis

## 🧠 Goal

Aggregate and compare risk and performance.

---

## 🔹 Sector Volatility

    sector_vol = df.pivot_table(
        index='date',
        columns='sector',
        values='vol',
        aggfunc='mean'
    )

---

## 🔹 Sector Returns

    sector_returns = df.pivot_table(
        index='date',
        columns='sector',
        values='return',
        aggfunc='mean'
    )

---

## 🔹 Risk Signal

    risk_signal = sector_vol > sector_vol.rolling(60).mean()

---

## 🧭 Output

- Time series of sector-level risk
- Identifiable volatility spikes

---

## 💡 Insight

Pivoting enables comparison across categories over time.