import pandas as pd

# 1. Membaca file CSV
df = pd.read_csv('Buku1.csv')

# 2. Mengubah format kolom 'Order Date' menjadi format tanggal
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Menghitung total 'Sales' per Hari, per Kota (City), dan per Kategori
rekap_kota = df.groupby(['Order Date', 'City', 'Category'])['Sales'].sum().reset_index()

# 4. Mengurutkan tabel berdasarkan Tanggal, lalu Kota secara alfabetis
rekap_kota = rekap_kota.sort_values(by=['Order Date', 'City', 'Category'])

# 5. Menampilkan 10 baris pertama di layar sebagai preview
print("--- Preview 10 Baris Pertama ---")
print(rekap_kota.head(10))

# 6. Menyimpan hasil rekap lengkap ke dalam file CSV baru
nama_file_baru = 'Rekap_Harian_Per_Kota.csv'
rekap_kota.to_csv(nama_file_baru, index=False)

print(f"\nSelesai! Seluruh data per tanggal dan kota telah berhasil disimpan di: {nama_file_baru}")