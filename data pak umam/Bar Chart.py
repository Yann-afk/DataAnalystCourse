import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Muat Data
df = pd.read_csv('Data_Cleaned_Format.csv')

# Set Tema
sns.set_theme(style="whitegrid")

# --- 1. BAR CHART: JUMLAH UNIT TERJUAL PER KATEGORI ---
plt.figure(figsize=(10, 6))
qty_category = df.groupby('Category')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False)

sns.barplot(x='Category', y='Quantity', data=qty_category, palette='viridis')
plt.title('Total Unit Terjual per Kategori', fontsize=14)
plt.ylabel('Jumlah Quantity')
plt.show()

# --- 2. BAR CHART: JUMLAH UNIT TERJUAL PER WILAYAH ---
plt.figure(figsize=(10, 6))
qty_region = df.groupby('Region')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False)

sns.barplot(x='Region', y='Quantity', data=qty_region, palette='magma')
plt.title('Total Unit Terjual per Wilayah (Region)', fontsize=14)
plt.ylabel('Jumlah Quantity')
plt.show()

# --- 3. RINGKASAN ANGKA ---
total_qty = df['Quantity'].sum()
avg_qty = df['Quantity'].mean()

print("\n" + "="*40)
print(f"ANALISIS VOLUME PENJUALAN (QUANTITY)")
print("="*40)
print(f"Total seluruh barang terjual : {int(total_qty)} unit")
print(f"Rata-rata barang per order   : {avg_qty:.2f} unit")
print("-" * 40)
print("\nDetail per Kategori:")
print(qty_category.to_string(index=False))
print("\n" + "="*40)