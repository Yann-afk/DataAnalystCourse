import pandas as pd
import matplotlib.pyplot as plt

# 1. Membaca file data
df = pd.read_csv('Data_Cleaned_Format.csv')

# 2. Menjumlahkan kuantitas penjualan per Wilayah (Region)
region_sales = df.groupby('Region')['Quantity'].sum().sort_values(ascending=False)

# 3. Hitung Total Keseluruhan (Grand Total) untuk semua produk
grand_total = region_sales.sum()

# 4. Membuat label kustom: "Nama Wilayah: Total Kuantitas"
labels_with_totals = [f'{reg}: {int(val)}' for reg, val in zip(region_sales.index, region_sales.values)]

# 5. Membuat Visualisasi Pie Chart
plt.figure(figsize=(10, 9))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'] # Warna kustom yang cerah

plt.pie(
    region_sales, 
    labels=labels_with_totals, 
    autopct='%1.1f%%',   
    startangle=140, 
    colors=colors,
    explode=[0.05] * len(region_sales), # Memberi sedikit jarak antar potongan
    pctdistance=0.80     
)

# 6. Menambahkan Judul Utama
plt.title('Proporsi & Total Penjualan per Wilayah', fontsize=16, fontweight='bold', pad=20)

# 7. Menambahkan teks "Total Semua Produk" di bagian bawah grafik
plt.text(0, -1.3, f'TOTAL KESELURUHAN PRODUK TERJUAL: {int(grand_total)}', 
         ha='center', fontsize=12, fontweight='bold', color='white', 
         bbox=dict(facecolor='#2c3e50', alpha=0.9, edgecolor='black', boxstyle='round,pad=0.6'))

# Menampilkan grafik
plt.tight_layout()
plt.show()