import pandas as pd

# ==========================================
# FASE 1: MEMBACA DATA
# ==========================================
print("Membaca file data...")
df = pd.read_csv('Buku1.csv')

# ==========================================
# FASE 2: DATA CLEANING (PEMBERSIHAN DATA)
# ==========================================
print("Memulai proses pembersihan data...")

# Menghapus duplikat
df = df.drop_duplicates()

# Menghapus baris yang kosong pada kolom penting (sekarang Quantity juga wajib ada)
df = df.dropna(subset=['Order Date', 'Sub-Category', 'Sales', 'Quantity'])

# Membersihkan teks Sub-Kategori
df['Sub-Category'] = df['Sub-Category'].astype(str).str.strip().str.title()

# Memastikan Sales dan Quantity adalah angka (Numeric)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df = df.dropna(subset=['Sales', 'Quantity']) # Hapus jika gagal diubah ke angka

# Memastikan Order Date adalah tanggal
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df = df.dropna(subset=['Order Date'])

print("Pembersihan data selesai!\n")

# ==========================================
# FASE 3: PENGOLAHAN DATA PIVOT (SALES & QUANTITY)
# ==========================================
print("Memulai rekapitulasi Pivot (Sales & Quantity)...")

# 1. Membuat kolom Tahun-Bulan ('2023-01')
df['Order Month'] = df['Order Date'].dt.strftime('%Y-%m')

# 2. Mengubah data menjadi bentuk Pivot dengan DUA values (Sales & Quantity)
rekap_pivot = pd.pivot_table(
    df, 
    values=['Sales', 'Quantity'], # Tambahkan Quantity di sini
    index='Order Month',          # Baris
    columns='Sub-Category',       # Kolom
    aggfunc='sum',                # Keduanya dijumlahkan (sum)
    fill_value=0                  # Mengisi angka 0 jika tidak ada transaksi
)

# 3. Merapikan nama kolom
# Karena kita menghitung 2 hal, Excel akan membuat tingkat kolom (Sales -> Buku, Quantity -> Buku).
# Kode di bawah ini berguna untuk menggabungkannya menjadi 1 baris judul, misal: "Bookcases (Quantity)"
rekap_pivot.columns = [f"{sub_cat} ({val})" for val, sub_cat in rekap_pivot.columns]
rekap_pivot = rekap_pivot.reset_index()

# ==========================================
# FASE 4: MENYIMPAN HASIL
# ==========================================

print("--- Preview 10 Baris Pertama ---")
print(rekap_pivot.head(10))

# Menyimpan hasil
nama_file_rekap = 'Rekap_Bulanan_Pivot_Lengkap.csv'
rekap_pivot.to_csv(nama_file_rekap, index=False)

print(f"\nSelesai! Data Sales & Quantity sudah berhasil disimpan di: {nama_file_rekap}")