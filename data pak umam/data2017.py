import pandas as pd
import plotly.express as px

# 1. Load Data
df = pd.read_csv('Data_Cleaned_Format.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 2. Urutkan data berdasarkan tanggal
df = df.sort_values('Order Date')

# 3. Kita buat Bar Chart agar filter tanggal terasa berguna
# Kita ambil Top 10 Kota agar tampilan tetap bersih
top_10_cities = df.groupby('City')['Profit'].sum().nlargest(10).index
df_filtered = df[df['City'].isin(top_10_cities)]

# Agregasi data per tanggal dan per kota
df_daily = df_filtered.groupby(['Order Date', 'City'])['Profit'].sum().reset_index()

# 4. Buat Grafik dengan Range Slider
fig = px.bar(
    df_daily, 
    x='Order Date', 
    y='Profit', 
    color='City',
    title='Total Profit per Kota Berdasarkan Rentang Tanggal',
    barmode='group'
)

# 5. Tambahkan Fitur Pemilih Tanggal (Range Slider & Selectors)
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True), # Ini yang membuat Anda bisa geser tanggal 1-10, dst
        type="date"
    ),
    yaxis_title="Total Profit",
    legend_title="Kota (Top 10)"
)

fig.show()