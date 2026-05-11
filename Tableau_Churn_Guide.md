# 📊 Tableau Churn Dashboard — Step-by-Step Guide
### FUTURE_DS_02 | Telco Customer Retention & Churn Analysis

---

## Prerequisites
- Tableau Public: https://public.tableau.com/en-us/s/download
- Dataset: `data/telco_customer_churn.csv`
- Colours: Orange `#FF6B2B` | Blue `#1E90FF` | Navy `#0D1B3E` | White `#FFFFFF` | Grey `#F0F2F5`

---

## Step 1 — Connect & Prep

1. Open Tableau → **Connect → Text File** → select `telco_customer_churn.csv`
2. Verify 7,043 rows
3. Change `SeniorCitizen` from Number to String
4. Create calculated field **Churned (0/1)**:
```
IF [Churn] = "Yes" THEN 1 ELSE 0 END
```
5. Create **Churn Rate %**:
```
SUM([Churned (0/1)]) / COUNT([Customer ID])
```
Format as Percentage, 1 decimal

6. Create **Tenure Band**:
```
IF [Tenure] <= 12 THEN "0-12 mo"
ELSEIF [Tenure] <= 24 THEN "13-24 mo"
ELSEIF [Tenure] <= 36 THEN "25-36 mo"
ELSEIF [Tenure] <= 48 THEN "37-48 mo"
ELSEIF [Tenure] <= 60 THEN "49-60 mo"
ELSE "61-72 mo"
END
```

7. Create **Senior Label**:
```
IF [Senior Citizen] = "1" THEN "Senior" ELSE "Non-Senior" END
```

---

## Step 2 — Chart 1: Churn by Contract Type (Bar)

1. Drag **Contract** to Columns
2. Drag **Churn Rate %** to Rows
3. Mark type: **Bar** → Color: Orange `#FF6B2B`
4. Sort descending
5. Add **Churn Rate %** to Label
6. Add reference line at 26.5% (overall average)
7. Title: `Churn Rate by Contract Type`

---

## Step 3 — Chart 2: Churn by Internet Service (Bar)

1. Drag **Internet Service** to Columns
2. Drag **Churn Rate %** to Rows
3. Mark type: **Bar** → Color: Blue `#1E90FF`
4. Title: `Churn Rate by Internet Service`
5. Add annotation on Fiber optic bar: "41.9% — Highest Risk Product"

---

## Step 4 — Chart 3: Tenure vs Churn (Line)

1. Drag **Tenure Band** to Columns (sort manually: 0-12, 13-24...)
2. Drag **Churn Rate %** to Rows
3. Mark type: **Line** → Color: Orange, thick
4. Add circle markers
5. Title: `Churn Rate Decreases Significantly With Tenure`

---

## Step 5 — Chart 4: Payment Method (Horizontal Bar)

1. Drag **Payment Method** to Rows
2. Drag **Churn Rate %** to Columns
3. Mark type: **Bar** → Color: gradient Navy to Orange by churn rate
4. Sort descending
5. Title: `Electronic Check Customers Churn at 45.3%`

---

## Step 6 — Chart 5: Cross-Segment Heatmap

1. Drag **Contract** to Columns
2. Drag **Internet Service** to Rows
3. Drag **Churn Rate %** to Color
4. Mark type: **Square**
5. Color palette: white (low) → orange (high)
6. Add **Churn Rate %** to Label
7. Title: `Churn Rate Heatmap: Contract x Internet Service`

---

## Step 7 — Chart 6: Add-on Services Impact (Grouped Bar)

1. Create a data union or calculated field comparing:
   - With Tech Support vs Without
   - With Online Security vs Without
2. Drag to grouped bar chart
3. Colors: Green (with add-on) vs Orange (without add-on)
4. Title: `Add-On Services Significantly Reduce Churn`

---

## Step 8 — Dashboard Layout

```
┌─────────────────────────────────────────────────────────┐
│  TITLE + KPI METRICS (text boxes)                       │
│  26.5% Churn | $139K/mo at Risk | 18mo Avg Tenure       │
├──────────────────┬──────────────────────────────────────┤
│  Contract Bar    │  Internet Service Bar                │
├──────────────────┼──────────────────────────────────────┤
│  Tenure Line     │  Payment Method Bar                  │
├──────────────────┴──────────────────────────────────────┤
│  Contract x Internet Heatmap (full width)               │
├──────────────────┬──────────────────────────────────────┤
│  Add-ons Impact  │  Senior vs Non-Senior Pie            │
└──────────────────┴──────────────────────────────────────┘
```

---

## Step 9 — Add Filters
- Contract Type (global filter → all worksheets)
- Internet Service
- Senior Citizen

---

## Step 10 — Publish
1. File → Save to Tableau Public
2. Name: `Telco Customer Churn Analysis — FUTURE_DS_02`
3. Add URL to README

---

## ✅ Verification Checklist

- [ ] Total = 7,043 customers
- [ ] Churn rate = 26.5%
- [ ] Month-to-month = 42.7% churn
- [ ] Fiber optic = 41.9% churn
- [ ] Electronic check = 45.3% churn
- [ ] Senior = 41.7% churn
- [ ] 0-12 months tenure = 47.4% churn
- [ ] Monthly revenue at risk = $139,131

---

## 🎨 Colour Reference

| Colour | Hex | Use |
|---|---|---|
| Orange | `#FF6B2B` | Primary — high churn, risk |
| Blue | `#1E90FF` | Secondary accent |
| Navy | `#0D1B3E` | Background, headers |
| White | `#FFFFFF` | Card backgrounds |
| Grey | `#F0F2F5` | Alternating rows |
| Green | `#22C55E` | Low churn, positive |
| Red | `#EF4444` | Critical alerts |

---

*Guide for FUTURE_DS_02 | Future Interns DS&A Track*
