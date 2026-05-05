import pandas as pd

# 1. Membaca file CSV Anda
# Pastikan file 'Buku1.csv' berada di folder yang sama dengan script Python ini
df = pd.read_csv('Buku1.csv')

# 2. Mengubah format kolom 'Order Date' menjadi format tanggal (datetime)
# Ini penting agar data bisa diurutkan secara kronologis (dari Januari hingga Desember)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Membuat tabel rekap (Pivot)
# Menghitung total 'Sales' (pendapatan) per hari untuk setiap 'Category'
tabel_pendapatan = pd.pivot_table(
    df, 
    values='Sales', 
    index='Order Date', 
    columns='Category', 
    aggfunc='sum', 
    fill_value=0  # Mengisi angka 0 jika tidak ada penjualan di kategori tersebut pada hari itu
)

# 4. Mengurutkan tabel berdasarkan tanggal dari yang paling awal
tabel_pendapatan = tabel_pendapatan.sort_index()

# 5. Menampilkan 10 hari pertama di layar sebagai preview
print("--- Preview 10 Hari Pertama ---")
print(tabel_pendapatan.head(10))

# 6. Menyimpan hasil rekap lengkap (ribuan baris) ke dalam file CSV baru
nama_file_baru = 'Rekap_Pendapatan_Harian.csv'
tabel_pendapatan.to_csv(nama_file_baru)

print(f"\nSelesai! Seluruh data per tanggal telah berhasil disimpan di file: {nama_file_baru}")
print("Anda bisa membuka file tersebut menggunakan Excel untuk melihat daftar lengkapnya.")