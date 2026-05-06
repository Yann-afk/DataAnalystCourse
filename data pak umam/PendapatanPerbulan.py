import pandas as pd

# 1. Membaca file CSV Anda
df = pd.read_csv('./data pak umam/Buku1.csv')

# 2. Mengubah format kolom 'Order Date' menjadi format tanggal (datetime)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# --- TAMBAHAN: Membuat kolom Bulan ---
# Kita buat kolom baru 'Order Month' agar data dikelompokkan per bulan (Tahun-Bulan)
df['Order Month'] = df['Order Date'].dt.to_period('M')

# 3. Membuat tabel rekap (Pivot) Bulanan
# Gunakan 'Order Month' sebagai index, bukan 'Order Date'
tabel_pendapatan_bulanan = pd.pivot_table(
    df, 
    values='Sales', 
    index='Order Month', 
    columns='Category', 
    aggfunc='sum', 
    fill_value=0
)

# 4. Mengurutkan tabel berdasarkan bulan
tabel_pendapatan_bulanan = tabel_pendapatan_bulanan.sort_index()

# 5. Menampilkan preview di layar
print("--- Rekap Pendapatan Per Bulan ---")
print(tabel_pendapatan_bulanan)

# 6. Menyimpan hasil ke file CSV baru
nama_file_baru = 'Rekap_Pendapatan_Bulanan.csv'
# Catatan: Kita gunakan .to_timestamp() agar format tanggal di Excel lebih ramah dibaca
tabel_pendapatan_bulanan.to_timestamp().to_csv(nama_file_baru)

print(f"\nSelesai! Data bulanan telah disimpan di: {nama_file_baru}")