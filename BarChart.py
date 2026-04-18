import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Muat Data
df = pd.read_csv('Data_Cleaned_Format.csv')

# Pastikan format tanggal benar
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)

# Set tema visualisasi
sns.set_theme(style="whitegrid")

# --- GRAFIK 1: PER WILAYAH (REGION) ---
plt.figure(figsize=(10, 6))
region_sales = df.groupby('Region')['Sales'].sum().reset_index().sort_values('Sales', ascending=False)
sns.barplot(x='Region', y='Sales', data=region_sales, palette='viridis')
plt.title('Total Penjualan per Wilayah', fontsize=14)
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()  # <--- Jendela ini harus ditutup untuk memunculkan grafik berikutnya

# --- GRAFIK 2: TOP 10 PRODUK ---
plt.figure(figsize=(12, 8))
top_products = df.groupby('Product Name')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(10)
sns.barplot(x='Sales', y='Product Name', data=top_products, palette='Blues_r')
plt.title('Top 10 Produk Berdasarkan Penjualan', fontsize=14)
plt.tight_layout()
plt.show()

# --- GRAFIK 3: SUB-KATEGORI (SUB PRODUK) ---
plt.figure(figsize=(10, 7))
sub_cat_sales = df.groupby('Sub-Category')['Sales'].sum().reset_index().sort_values('Sales', ascending=False)
sns.barplot(x='Sales', y='Sub-Category', data=sub_cat_sales, palette='magma')
plt.title('Penjualan per Sub-Kategori', fontsize=14)
plt.tight_layout()
plt.show()

# --- GRAFIK 4: PENDAPATAN PER BULAN ---
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby('Month-Year')['Sales'].sum().reset_index()
# Menampilkan 15 bulan terakhir agar tren lebih terlihat
monthly_sales = monthly_sales.tail(15) 
sns.barplot(x='Month-Year', y='Sales', data=monthly_sales, palette='rocket')
plt.title('Tren Penjualan Bulanan (15 Bulan Terakhir)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()