import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Muat Data
df = pd.read_csv('Data_Cleaned_Format.csv')

# Persiapan data tanggal
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.strftime('%B')
df['Year'] = df['Order Date'].dt.year

# Set Tema Visualisasi
sns.set_theme(style="white")

# --- 1. PIE CHART: WILAYAH (REGION) ---
plt.figure(figsize=(10, 7))
region_data = df.groupby('Region')['Sales'].sum()

plt.pie(
    region_data, 
    labels = region_data.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette('pastel'),
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Proporsi Penjualan per Wilayah (Region)', fontsize=14, pad=20)
plt.axis('equal')
plt.show()

# --- 2. PIE CHART: KATEGORI PRODUK ---
plt.figure(figsize=(10, 7))
category_data = df.groupby('Category')['Sales'].sum()

plt.pie(
    category_data, 
    labels = category_data.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=sns.color_palette('Set3'),
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Proporsi Penjualan per Kategori Utama', fontsize=14, pad=20)
plt.axis('equal')
plt.show()

# --- 3. PIE CHART: PENDAPATAN PER BULAN (Tahun Terakhir) ---
latest_year = df['Year'].max()
df_last_year = df[df['Year'] == latest_year]

# Hitung penjualan per bulan & urutkan sesuai kalender
monthly_data = df_last_year.groupby('Month')['Sales'].sum()
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
monthly_data = monthly_data.reindex(months_order).fillna(0)

plt.figure(figsize=(12, 8))
plt.pie(
    monthly_data, 
    labels = monthly_data.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette('husl', 12),
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)

# Donut Chart effect
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title(f'Persentase Kontribusi Penjualan per Bulan (Tahun {latest_year})', fontsize=15, pad=20)
plt.axis('equal') 
plt.tight_layout()
plt.show()

# --- 4. ANALISIS PERTUMBUHAN (OUTPUT TEXT) ---
annual_growth = df.groupby('Year')['Sales'].sum()

print("\n" + "="*40)
print(f"HASIL ANALISIS PENDAPATAN")
print("="*40)
print("\n--- Ringkasan Total Penjualan per Tahun ---")
print(annual_growth.apply(lambda x: f"${x:,.2f}"))

print("\n--- Persentase Pertumbuhan Tahunan ---")
growth_pct = annual_growth.pct_change() * 100
print(growth_pct.apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "Base Year"))
print("\n" + "="*40)