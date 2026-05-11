# Telco Customer Retention & Churn Analysis
**Future Interns | Data Science & Analytics | Task 2 — FUTURE_DS_02**

![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20Tableau%20%7C%20Google%20Sheets-orange?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-IBM%20Watson%20Telco-blue?style=flat-square)
![Churn Rate](https://img.shields.io/badge/Churn%20Rate-26.5%25-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## What this project is about

For Task 2 I analysed a telecommunications company's customer data to understand why customers are leaving and what the business can do about it. The dataset comes from IBM and covers 7,043 customers with details on their contracts, services, billing, and whether they eventually churned.

The overall churn rate is 26.5% — meaning more than 1 in 4 customers left. That translates to $139,131 in monthly recurring revenue walking out the door.

---

## Dataset

**Source:** IBM Watson Telco Customer Churn — [Kaggle link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

7,043 customers, 21 columns including contract type, internet service, payment method, tenure, monthly charges, add-on services, and whether the customer churned.

One data quality note: TotalCharges had blank values for customers with zero tenure (brand new customers). I converted it to numeric and filled those blanks with the median before doing any analysis.

---

## Tools I used

- **Excel** — main dashboard with 6 charts, KPI cards, and cross-segment tables
- **Tableau** — interactive dashboard (build guide in /docs)
- **Google Sheets** — pivot tables and initial exploration
- **Python** — validation script to confirm all my numbers are right

---

## Folder structure

```
FUTURE_DS_02/
├── data/
│   ├── telco_customer_churn.csv
│   └── FUTURE_DS_02_Telco_Churn_Analysis.xlsx
├── scripts/
│   └── churn_analysis.py
├── docs/
│   ├── Tableau_Churn_Guide.md
│   └── Google_Sheets_Guide.md
├── screenshots/
└── README.md
```

---

## Key numbers

| Metric | Value |
|---|---|
| Total customers | 7,043 |
| Churned | 1,869 (26.5%) |
| Retained | 5,174 (73.5%) |
| Monthly revenue at risk | $139,131 |
| Avg monthly charge — churned | $74.44 |
| Avg monthly charge — retained | $61.27 |
| Avg tenure — churned | 18.0 months |
| Avg tenure — retained | 37.6 months |

---

## Main findings

**Contract type is the single strongest predictor of churn.** Month-to-month customers churn at 42.7%, compared to 11.3% for one-year and just 2.8% for two-year contracts. Yet over half the customer base (3,875 people) is still on month-to-month plans.

**Fiber optic is the most at-risk product at 41.9% churn.** Fiber customers pay the most ($91.50/month on average) but are the most likely to leave. When I looked at why, I found that Fiber customers without Online Security churn at 49.4% — almost half. With security, it drops to 21.8%. The product needs better value bundling.

**Electronic check users churn at 45.3% — nearly triple auto-pay customers.** Bank transfer and credit card customers churn at 15-17%. Manual payment is a strong signal of disengagement.

**Senior citizens churn at 41.7% and pay the most.** The average senior pays $79.82/month but churns at 77% higher than non-seniors. Seniors on month-to-month contracts specifically churn at 54.6%.

**Tech Support is a retention anchor.** Without it: 41.6% churn. With it: 15.2% churn. Same pattern holds for Online Security (41.8% vs 14.6%). These add-ons are not just revenue — they keep customers.

**Almost half of year-one customers leave (47.4%).** After 5 years the rate drops to 6.6%. Onboarding is clearly a problem.

---

## Cross-segment findings (the interesting ones)

These combinations were the most revealing part of my analysis:

| Segment | Churn Rate | No. of Customers |
|---|---|---|
| Month-to-month + Fiber optic | 54.6% | 2,128 |
| Senior + Month-to-month | 54.6% | 807 |
| Month-to-month + Electronic check | 53.7% | 1,850 |
| Two-year + DSL | 1.9% | 628 |
| With Tech Support | 15.2% | 2,044 |

---

## Recommendations

1. Offer a discount to move month-to-month customers onto annual contracts — even 10% off would save a lot
2. Bundle Online Security or Tech Support into Fiber optic plans to reduce the 49.4% churn rate
3. Incentivise auto-pay sign-up with a small monthly credit (e.g. $5 off for switching from electronic check)
4. Create a dedicated retention programme for senior citizens, especially those on Fiber and month-to-month
5. Start a proper onboarding programme — call new customers at day 7, 30, and 90 to catch issues early

---

## How to run the Python script

```bash
pip install pandas
python scripts/churn_analysis.py
```

---

## Limitations

- This is a snapshot dataset — there is no time dimension so I cannot track how churn evolved over months
- I do not know the actual reason any customer left — exit survey data would make this much stronger
- Revenue impact is based on monthly charges, not actual LTV

---

## What I learned

The cross-segment analysis was the most valuable part for me. Looking at churn by contract type alone is useful, but when I combined it with internet service type I found that some segments are nearly 55% likely to churn. That is a very different finding from the 26.5% headline rate and changes what you would prioritise.

I also learned that add-on services matter a lot more than I expected going in. I initially thought they were just extra revenue, but the churn difference between customers with and without Tech Support is dramatic. Retention and upselling are actually the same strategy here.

The hardest part was the cross-segment pivot tables in Excel — getting them to update correctly took some time but it was worth it for the insight it produced.

---

## About

**Intern:** Khanyisile | Johannesburg, South Africa
**Programme:** Future Interns Data Science & Analytics Internship
**GitHub:** [github.com/khanyisiletshabalala](https://github.com/khanyisiletshabalala)
