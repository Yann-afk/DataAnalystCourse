import pandas as pd
import matplotlib.pyplot as plt

# 1. Memuat data
df = pd.read_csv('Data_Cleaned_Format.csv')

# 2. Menghitung total penjualan (Quantity) per Produk
sales_by_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

# 3. Membuat visualisasi
plt.figure(figsize=(10, 6))
bars = plt.bar(sales_by_product.index, sales_by_product.values, color='skyblue', edgecolor='navy')

# 4. Menambahkan angka (label) di atas setiap bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# 5. Menambah detail grafik
plt.title('Total Penjualan Berdasarkan Produk', fontsize=14)
plt.xlabel('Produk', fontsize=12)
plt.ylabel('Total Kuantitas Terjual', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan grafik
plt.tight_layout()
plt.show()