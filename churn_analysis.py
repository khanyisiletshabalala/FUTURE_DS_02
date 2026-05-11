# Task 2 - Customer Retention & Churn Analysis
# Dataset: IBM Watson Telco Customer Churn (Kaggle)
# Author: Khanyisile
# Future Interns - Data Science & Analytics

# pip install pandas before running this

import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'telco_customer_churn.csv')

print("\nLoading churn dataset...")

try:
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df):,} customer records")
except FileNotFoundError:
    print(f"File not found at: {DATA_PATH}")
    print("Make sure telco_customer_churn.csv is in the /data folder")
    exit()

# TotalCharges has some blank values for customers with 0 tenure
# I noticed this when I got NaN errors - fixed by converting then filling
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# make churn numeric so I can do maths on it
df['Churned'] = (df['Churn'] == 'Yes').astype(int)

# easier label for senior citizen
df['Senior'] = df['SeniorCitizen'].map({1: 'Senior', 0: 'Non-Senior'})

# tenure bands - took me a bit to figure out the right bin edges
df['Tenure Band'] = pd.cut(df['tenure'],
    bins=[0, 12, 24, 36, 48, 60, 72],
    labels=['0-12 mo', '13-24 mo', '25-36 mo', '37-48 mo', '49-60 mo', '61-72 mo'])

total    = len(df)
churned  = df['Churned'].sum()
retained = total - churned
rate     = churned / total * 100

print(f"\nTotal: {total:,} | Churned: {churned:,} | Retained: {retained:,}")
print(f"Overall churn rate: {rate:.1f}%")
print(f"Monthly revenue at risk: ${df[df['Churn']=='Yes']['MonthlyCharges'].sum():,.2f}")

# checking for nulls after cleaning
remaining_nulls = df.isnull().sum()
remaining_nulls = remaining_nulls[remaining_nulls > 0]
if len(remaining_nulls) > 0:
    print(f"\nStill have nulls in: {remaining_nulls.to_dict()}")
else:
    print("No nulls remaining after cleaning")

print("\n" + "-"*60)
print("CHURN BY CONTRACT TYPE")
print("-"*60)
# this was my biggest finding - month to month is really bad
con = df.groupby('Contract').agg(
    Customers=('Churned', 'count'),
    Churned=('Churned', 'sum'),
    ChurnRate=('Churned', 'mean')
).round(3)

for idx, row in con.iterrows():
    note = " <- BIG PROBLEM" if row['ChurnRate'] > 0.35 else ""
    print(f"  {idx:<20} {int(row['Customers']):>5,} customers  "
          f"{row['ChurnRate']*100:.1f}% churn{note}")

print("\n" + "-"*60)
print("CHURN BY INTERNET SERVICE")
print("-"*60)
isp = df.groupby('InternetService').agg(
    Customers=('Churned', 'count'),
    ChurnRate=('Churned', 'mean'),
    AvgCharge=('MonthlyCharges', 'mean')
).round(3)

for idx, row in isp.iterrows():
    print(f"  {idx:<15} {int(row['Customers']):>5,} customers  "
          f"{row['ChurnRate']*100:.1f}% churn  avg charge: ${row['AvgCharge']:.2f}/mo")

print("\n" + "-"*60)
print("CHURN BY PAYMENT METHOD")
print("-"*60)
pay = df.groupby('PaymentMethod')['Churned'].agg(['mean', 'count']).round(3)
for idx, row in pay.iterrows():
    flag = " <- highest risk" if row['mean'] > 0.40 else ""
    print(f"  {idx:<35} {row['mean']*100:.1f}% churn{flag}")

print("\n" + "-"*60)
print("CHURN BY TENURE BAND")
print("-"*60)
# interesting how much tenure matters - year 1 is really when people leave
ten = df.groupby('Tenure Band', observed=True)['Churned'].agg(['mean', 'count']).round(3)
for idx, row in ten.iterrows():
    bar = '#' * int(row['mean'] * 20)
    print(f"  {str(idx):<12} {bar:<20} {row['mean']*100:.1f}% ({int(row['count']):,} customers)")

print("\n" + "-"*60)
print("ADD-ON SERVICES IMPACT")
print("-"*60)
# this surprised me - tech support makes a massive difference
for col, label in [('TechSupport', 'Tech Support'), ('OnlineSecurity', 'Online Security')]:
    grp = df.groupby(col)['Churned'].agg(['mean', 'count']).round(3)
    print(f"\n  {label}:")
    for idx, row in grp.iterrows():
        print(f"    {str(idx):<25} {row['mean']*100:.1f}% churn  ({int(row['count']):,} customers)")

print("\n" + "-"*60)
print("CROSS SEGMENT: CONTRACT x INTERNET")
print("-"*60)
# the worst combination is month-to-month + fiber optic
cross = df.groupby(['Contract', 'InternetService'])['Churned'].agg(['mean', 'count']).round(3)
for (c, i), row in cross.iterrows():
    flag = " <- WORST SEGMENT" if row['mean'] > 0.50 else ""
    print(f"  {c+' + '+i:<42} {row['mean']*100:.1f}% ({int(row['count']):,}){flag}")

print("\n" + "-"*60)
print("SENIOR CITIZENS")
print("-"*60)
sen = df.groupby('Senior').agg(
    Customers=('Churned', 'count'),
    ChurnRate=('Churned', 'mean'),
    AvgCharge=('MonthlyCharges', 'mean')
).round(3)
for idx, row in sen.iterrows():
    print(f"  {idx:<15} {int(row['Customers']):>5,} customers  "
          f"{row['ChurnRate']*100:.1f}% churn  avg ${row['AvgCharge']:.2f}/mo")

print("\n" + "-"*60)
print("AVERAGE PROFILE: CHURNED vs RETAINED")
print("-"*60)
profile = df.groupby('Churn')[['tenure', 'MonthlyCharges', 'TotalCharges']].mean().round(2)
for col in profile.columns:
    v_no  = profile.loc['No', col]
    v_yes = profile.loc['Yes', col]
    diff  = v_yes - v_no
    print(f"  {col:<20} Retained: {v_no:>8.2f}  Churned: {v_yes:>8.2f}  diff: {diff:>+8.2f}")

print("\n" + "-"*60)
print("CHECK THESE AGAINST YOUR DASHBOARD")
print("-"*60)
print(f"""
  Total customers          : {total:,}
  Churned                  : {churned:,}
  Churn rate               : {rate:.1f}%
  Monthly revenue at risk  : ${df[df['Churn']=='Yes']['MonthlyCharges'].sum():,.2f}
  Month-to-month churn     : {df[df['Contract']=='Month-to-month']['Churned'].mean()*100:.1f}%
  Fiber optic churn        : {df[df['InternetService']=='Fiber optic']['Churned'].mean()*100:.1f}%
  Electronic check churn   : {df[df['PaymentMethod']=='Electronic check']['Churned'].mean()*100:.1f}%
  Senior churn             : {df[df['SeniorCitizen']==1]['Churned'].mean()*100:.1f}%
  Year 1 churn (0-12 mo)   : {df[df['tenure']<=12]['Churned'].mean()*100:.1f}%
  No tech support churn    : {df[df['TechSupport']=='No']['Churned'].mean()*100:.1f}%
  With tech support churn  : {df[df['TechSupport']=='Yes']['Churned'].mean()*100:.1f}%
""")
