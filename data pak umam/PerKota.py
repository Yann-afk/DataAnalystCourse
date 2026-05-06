import pandas as pd
import os

# 1. Penanganan Lokasi File
file_input = './data pak umam/Buku1.csv'
file_output = 'Top10_Kota_Rekap_Horizontal.csv'

if not os.path.exists(file_input):
    print(f"ALERT: File '{file_input}' tidak ditemukan.")
else:
    print("Membaca data...")
    df = pd.read_csv(file_input)

    # 2. Data Cleaning
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df = df.dropna(subset=['Order Date', 'City', 'Category', 'Sales', 'Quantity'])

    # --- TAMBAHAN: MENCARI TOP 10 KOTA ---
    # Hitung total sales per kota
    top_10_cities = df.groupby('City')['Sales'].sum().nlargest(10).index
    
    # Filter dataframe asli agar hanya berisi 10 kota tersebut
    df = df[df['City'].isin(top_10_cities)]
    # -------------------------------------

    # 3. Membuat kolom format Bulan (Tahun-Bulan)
    df['Order Month'] = df['Order Date'].dt.strftime('%Y-%m')

    # 4. Membuat Pivot Table
    print("Memproses rekapitulasi horizontal untuk Top 10 Kota...")
    rekap_pivot = pd.pivot_table(
        df, 
        values=['Sales', 'Quantity'], 
        index=['City', 'Category'], 
        columns='Order Month',      
        aggfunc='sum', 
        fill_value=0 
    )

    # 5. Merapikan Header Kolom
    rekap_pivot.columns = [f"{month} ({val})" for val, month in rekap_pivot.columns]
    rekap_pivot = rekap_pivot.reset_index()

    # 6. Menyimpan ke CSV
    rekap_pivot.to_csv(file_output, index=False)

    print("-" * 30)
    print(f"BERHASIL!")
    print(f"Hanya data dari 10 kota dengan penjualan tertinggi yang diproses.")
    print(f"Hasil disimpan di: {file_output}")
    print("-" * 30)
    
    print("\nPreview Top 10 Kota (5 Baris Pertama):")
    print(rekap_pivot.head())