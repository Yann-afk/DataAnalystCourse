import pandas as pd

df = pd.read_csv('Data_Cleaned_Format.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Bandingkan total penjualan tahun 2016 vs 2017
sales_comparison = df[df['Order Date'].dt.year.isin([2016, 2017])].groupby(df['Order Date'].dt.year)['Sales'].sum()

print("--- Perbandingan Penjualan ---")
print(sales_comparison)

# Cek bulan terakhir yang ada di data 2017
last_date = df[df['Order Date'].dt.year == 2017]['Order Date'].max()
print(f"\nData tahun 2017 terakhir tercatat pada: {last_date}")