import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('Data_Cleaned_Format.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Set tema visual
sns.set_theme(style="whitegrid")
plt.figure(figsize=(16, 12))

# --- 1. COLUMN CHART (Total Quantity per Product) ---
plt.subplot(2, 2, 1)
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
sns.barplot(x=product_sales.index, y=product_sales.values, palette='magma')
plt.title('Total Quantity Terjual per Produk', fontsize=14)
plt.xticks(rotation=45)

# --- 2. PIE CHART (Revenue by Region) ---
plt.subplot(2, 2, 2)
region_dist = df.groupby('Region')['TotalPrice'].sum()
plt.pie(region_dist, labels=region_dist.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3'))
plt.title('Proporsi Pendapatan per Wilayah', fontsize=14)

# --- 3. LINE CHART (Tren Penjualan PER PRODUK) ---
plt.subplot(2, 1, 2)

# Mengelompokkan data berdasarkan Bulan dan Produk
# Kita hitung rata-rata atau total 'TotalPrice' per produk setiap bulannya
df_line = df.groupby([pd.Grouper(key='Date', freq='ME'), 'Product'])['TotalPrice'].sum().unstack()

# Plotting setiap kolom (produk) menjadi satu garis
for product in df_line.columns:
    plt.plot(df_line.index, df_line[product], marker='', linewidth=2, label=product)

plt.title('Tren Penjualan Bulanan per Produk', fontsize=14)
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan ($)')
plt.legend(title='Produk', bbox_to_anchor=(1.05, 1), loc='upper left') # Legenda di luar grafik
plt.grid(True, alpha=0.3)

# Mengatur tata letak agar rapi
plt.tight_layout()
plt.show()