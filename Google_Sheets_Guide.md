# 📋 Google Sheets Guide — Telco Churn Analysis
### FUTURE_DS_02 | Telco Customer Retention & Churn Analysis

---

## Step 1 — Upload
1. sheets.google.com → New → Upload → `telco_customer_churn.csv`
2. Rename tab: **Raw Data** | Freeze Row 1

---

## Step 2 — Helper Columns

| Header | Formula (Row 2) |
|---|---|
| Churned | `=IF(U2="Yes",1,0)` |
| Senior Label | `=IF(C2=1,"Senior","Non-Senior")` |
| Tenure Band | `=IFS(F2<=12,"0-12 mo",F2<=24,"13-24 mo",F2<=36,"25-36 mo",F2<=48,"37-48 mo",F2<=60,"49-60 mo",TRUE,"61-72 mo")` |
| Charge Band | `=IFS(S2<=30,"<$30",S2<=50,"$30-50",S2<=70,"$50-70",S2<=90,"$70-90",TRUE,"$90+")` |

---

## Step 3 — Pivot Tables

**Pivot 1: Contract Type**
- Rows: Contract | Values: CustomerID (COUNTA), Churned (SUM + AVERAGE as %)

**Pivot 2: Internet Service**
- Rows: InternetService | Values: CustomerID (COUNTA), Churned (SUM + AVERAGE)

**Pivot 3: Payment Method**
- Rows: PaymentMethod | Values: Churned (AVERAGE as %)

**Pivot 4: Tenure Band**
- Rows: Tenure Band | Values: Churned (AVERAGE as %)

**Pivot 5: Senior x Contract (Cross-Segment)**
- Rows: Senior Label | Columns: Contract | Values: Churned (AVERAGE)

---

## Step 4 — Charts
- Contract: Column chart, Orange
- Tenure: Line chart, Orange (shows declining churn over time)
- Payment: Bar chart, Navy
- Senior x Contract: Grouped bar, Orange vs Blue

---

## ✅ Verification

| Metric | Value |
|---|---|
| Total customers | 7,043 |
| Churned | 1,869 (26.5%) |
| Month-to-month churn | 42.7% |
| Fiber optic churn | 41.9% |
| Electronic check churn | 45.3% |
| Senior churn | 41.7% |
| 0-12 mo tenure churn | 47.4% |

---

*Guide for FUTURE_DS_02 | Future Interns DS&A Track*
