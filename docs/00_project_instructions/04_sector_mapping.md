# 🏷️ Sector Mapping

## 🧠 Goal

Add categorical information for analysis.

---

## 🔹 Create Mapping

    sector_map = {
        'SPY':'Market',
        'QQQ':'Tech',
        'TLT':'Bonds',
        'GLD':'Gold',
        '^VIX':'Volatility'
    }

---

## 🔹 Convert to DataFrame

    sector_df = pd.DataFrame(
        list(sector_map.items()),
        columns=['ticker','sector']
    )

---

## 🔹 Merge

    df = df.merge(sector_df, on='ticker')

---

## 🧭 Result

| date | ticker | sector | return | vol | momentum |

---

## 💡 Insight

Categorical data enables grouping and aggregation.