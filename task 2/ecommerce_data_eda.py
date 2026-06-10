import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\task 2\cleaned_ecommerce.csv')





#BASIC STATISTICS
print("\n=== BASIC STATISTICS ===")
#print(df.describe())

print("\n=== MEAN ===")
print(df.mean(numeric_only=True).round(2))

print("\n=== MEDIAN ===")
print(df.median(numeric_only=True).round(2))

print("\n=== count ===")
print(df.count(numeric_only=True))





# Dataset Overview
print("\n=== DATASET OVERVIEW ===")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Stats:\n", df.describe())





# === DISTRIBUTIONS ===
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Distribution of Numeric Columns', fontsize=16)

sns.histplot(df['TotalPrice'], kde=True, ax=axes[0,0], color='blue')
axes[0,0].set_title('TotalPrice Distribution')

sns.histplot(df['UnitPrice'], kde=True, ax=axes[0,1], color='green')
axes[0,1].set_title('UnitPrice Distribution')

sns.histplot(df['Quantity'], kde=True, ax=axes[1,0], color='orange')
axes[1,0].set_title('Quantity Distribution')

sns.histplot(df['ItemsInCart'], kde=True, ax=axes[1,1], color='red')
axes[1,1].set_title('ItemsInCart Distribution')

plt.tight_layout()
plt.savefig(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\task 2\distributions.png', dpi=150)
#plt.savefig('distributions.png', dpi=150)
plt.show()
print("Distribution chart saved!")





# === OUTLIERS — BOXPLOT ===
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Outlier Detection — Boxplots', fontsize=16)

sns.boxplot(y=df['TotalPrice'], ax=axes[0], color='blue')
axes[0].set_title('TotalPrice Outliers')

sns.boxplot(y=df['UnitPrice'], ax=axes[1], color='green')
axes[1].set_title('UnitPrice Outliers')

plt.tight_layout()
plt.savefig(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\task 2\outliers.png', dpi=150)
#plt.savefig('outliers.png', dpi=150)
plt.show()
print("Outlier chart saved!")



# === IQR OUTLIER DETECTION ===
print("\n=== IQR OUTLIER DETECTION ===")
for col in ['TotalPrice', 'UnitPrice', 'Quantity', 'ItemsInCart']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: {len(outliers)} outliers | Lower: {lower:.2f} | Upper: {upper:.2f}")





# === TRENDS — SALES OVER TIME ===
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\task 2\trends.png', dpi=150)
plt.show()
print("Trends chart saved!")




# === KEY OBSERVATIONS ===
print("\n" + "="*50)
print("KEY OBSERVATIONS — E-COMMERCE EDA REPORT")
print("="*50)

print("""
DATASET OVERVIEW:
- Total Orders: 1,200
- Total Columns: 14
- Missing Values: None (Clean Dataset)

BASIC STATISTICS:
- Average Order Value (TotalPrice): $1,053.97
- Median Order Value: $823.62
- Average Unit Price: $356.41
- Average Quantity per Order: 2.95 items

DISTRIBUTION INSIGHTS:
- TotalPrice is RIGHT SKEWED — majority of orders 
  are in low price range ($0-$500)
- UnitPrice is UNIFORMLY distributed — all price 
  ranges equally represented
- Quantity is UNIFORM — customers order 1-5 items equally

OUTLIER DETECTION (IQR Method):
- TotalPrice: 8 outliers detected (above $3,330)
- These are HIGH VALUE orders — possible VIP/Bulk buyers
- UnitPrice, Quantity, ItemsInCart: No outliers found

SALES TREND:
- Peak Sales: June 2024 (~$68,000)
- Lowest Sales: March 2023 & June 2024 (~$28,000)
- Sales show fluctuating pattern — no consistent growth
- May/June appear to be peak months every year

BUSINESS RECOMMENDATIONS:
- Focus marketing on budget customers ($0-$500 range)
- Investigate 8 high-value outlier orders — VIP program?
- Boost inventory in May/June for peak season demand
""")
print("="*50)
print("EDA Complete!")