# 🔄 Reshape & Merge

## 🧠 Goal

Convert wide data into long format and combine datasets.

---

## 🔹 Convert to Long Format

    returns_long = returns.stack().reset_index()
    returns_long.columns = ['date','ticker','return']

---

## 🔹 Merge Datasets

    df = returns_long.merge(vol_long, on=['date','ticker'])
    df = df.merge(momentum_long, on=['date','ticker'])

---

## 🧭 Result

| date | ticker | return | vol | momentum |

---

## 💡 Insight

Merging creates a unified dataset for analysis.