import pandas as pd

# 1. Membaca file CSV
df = pd.read_csv('Buku1.csv')

# 2. Mengubah format kolom 'Order Date' menjadi format tanggal
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Menghitung total 'Sales' per Hari dan per Sub-Kategori
# Kita menggunakan kolom 'Sub-Category' sesuai dengan header di data Anda
rekap_sub_kategori = df.groupby(['Order Date', 'Sub-Category'])['Sales'].sum().reset_index()

# 4. Mengurutkan tabel berdasarkan Tanggal, lalu Sub-Kategori secara alfabetis
rekap_sub_kategori = rekap_sub_kategori.sort_values(by=['Order Date', 'Sub-Category'])

# 5. Menampilkan 10 baris pertama di layar sebagai preview
print("--- Preview 10 Baris Pertama ---")
print(rekap_sub_kategori.head(10))

# 6. Menyimpan hasil rekap lengkap ke dalam file CSV baru
nama_file_baru = 'Rekap_Harian_Per_Sub_Kategori.csv'
rekap_sub_kategori.to_csv(nama_file_baru, index=False)

print(f"\nSelesai! Seluruh data per tanggal dan sub-kategori telah berhasil disimpan di: {nama_file_baru}")