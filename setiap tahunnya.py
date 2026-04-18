import pandas as pd

df = pd.read_csv('Data_Cleaned_Format.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Menghitung total penjualan per tahun
annual_growth = df.groupby(df['Order Date'].dt.year)['Sales'].sum()

print("--- Ringkasan Pertumbuhan Tahunan ---")
print(annual_growth)
print("\n--- Pertumbuhan Persentase ---")
print(annual_growth.pct_change() * 100)