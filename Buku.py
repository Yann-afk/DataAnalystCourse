import pandas as pd
import numpy as np

# 1. Memuat dataset
df = pd.read_csv('Buku1.csv')

# 2. Hapus Duplikat
df.drop_duplicates(inplace=True)

# 3. Tangani Missing Values (Data Kosong)
# Mengisi Quantity yang kosong dengan 0
df['Quantity'] = df['Quantity'].fillna(0)
# Mengisi Sales (Pengganti UnitPrice) dengan nilai rata-rata
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
# Mengisi Profit yang kosong dengan 0 (Sebagai pengganti TotalPrice)
df['Profit'] = df['Profit'].fillna(0)

# 4. Standarisasi Format
# Menyeragamkan teks pada kolom Region dan Product Name
df['Region'] = df['Region'].astype(str).str.strip().str.title()
df['Product Name'] = df['Product Name'].astype(str).str.strip().str.title()

# 5. Hapus Outlier yang Tidak Masuk Akal
# Menggunakan kolom Sales untuk filter harga
df = df[(df['Sales'] > 0) & (df['Sales'] < 20000)]

# 6. Perbaiki Tipe Data
# Memastikan kolom numerik benar-benar angka
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

# Memperbaiki tipe data tanggal (Order Date & Ship Date)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# 7. Simpan hasil
df.to_csv('Data_Cleaned_Format.csv', index=False)

print("Proses cleaning selesai!")
print(df.info())