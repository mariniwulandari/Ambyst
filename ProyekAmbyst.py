import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visualisasi Data Covid-19")
st.image("Covid.jpg")
st.write("oleh Kelompok Ambyst")
st.write("""Nama kelompok:
1. Gabriella Natalie (021002214005)
2. Marini Wulandari (021002214006)
3. Meita Indah Fadilla (021002214007)
4. Muhammad Rizki (021002214008)

S1 Ekonomi Pembangunan""")

df = pd.read_csv('Data_Covid19_Kelompok_Ambyst.csv')
#df = pd.read_csv('Data_Covid19_Kelompok_Ambyst.csv')


st.write("## 5 data pertama")
st.write( df.head() )

st.write("## Info Data")
st.write( df.describe() )

# Load data dari CSV
file_path = "Data_Covid19_Kelompok_Ambyst.csv"  # Menggunakan nama file "Data_Covid19_Kelompok_Ambyst.csv"
data = pd.read_csv(file_path)

# Konversi kolom 'date' ke tipe data datetime
data['date'] = pd.to_datetime(data['date'])

# Membuat histogram menggunakan Plotly Express
def create_histogram_total_cases():
    fig = px.histogram(data, x='date', y='total_cases', title='Histogram Total Cases per Date')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Cases')
    return fig

def create_histogram_total_deaths():
    fig = px.histogram(data, x='date', y='total_deaths', title='Histogram Total Deaths per Date')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Deaths')
    return fig

# Menampilkan hasil di Streamlit
st.title('Histogram Total Cases and Total Deaths per Date')
st.write("Data Awal:")
st.write(data.head())

histogram_cases = create_histogram_total_cases()
st.plotly_chart(histogram_cases)

histogram_deaths = create_histogram_total_deaths()
st.plotly_chart(histogram_deaths)

# Mendapatkan total total_cases, total_deaths, dan population secara keseluruhan
total_cases_total = data['total_cases'].sum()
total_deaths_total = data['total_deaths'].sum()
total_population_total = data['population'].sum()

# Membuat DataFrame baru untuk pie chart
pie_data_total = pd.DataFrame({
    'Categories': ['Total Cases', 'Total Deaths', 'Total Population'],
    'Values': [total_cases_total, total_deaths_total, total_population_total]
})


# Membuat pie chart perbandingan total_cases, total_deaths, dan total_population secara keseluruhan
fig_pie_total = px.pie(pie_data_total, values='Values', names='Categories', title='Comparison of Cases, Deaths, and Population Overall')

# Menampilkan pie chart di Streamlit
st.title('Comparison of Cases, Deaths, and Population Overall')
st.plotly_chart(fig_pie_total)

# Menampilkan rincian total_cases dan total_deaths secara keseluruhan
st.write(f"Total Kasus secara total: {total_cases_total}")
st.write(f"Total Kematian secara total: {total_deaths_total}")

# Menampilkan pilihan negara di dropdown
available_countries = data['location'].unique()
selected_country = st.selectbox('Select Country', available_countries)

# Filter data berdasarkan negara yang dipilih
filtered_data = data[data['location'] == selected_country]

# Membuat histogram total_cases, total_deaths, dan population menggunakan Plotly Express
fig_cases = px.histogram(filtered_data, x='date', y='total_cases', title=f'Histogram Total Cases for {selected_country}')
fig_cases.update_layout(xaxis_title='Date', yaxis_title='Total Cases')

fig_deaths = px.histogram(filtered_data, x='date', y='total_deaths', title=f'Histogram Total Deaths for {selected_country}')
fig_deaths.update_layout(xaxis_title='Date', yaxis_title='Total Deaths')

fig_population = px.histogram(filtered_data, x='date', y='population', title=f'Histogram Population for {selected_country}')
fig_population.update_layout(xaxis_title='Date', yaxis_title='Population')

# Meita : Menampilkan hasil di Streamlit
st.title(f'Histograms for {selected_country}')
st.write("Data Awal:")
st.write(filtered_data.head())

st.subheader('Histogram Total Cases')
st.plotly_chart(fig_cases)

st.subheader('Histogram Total Deaths')
st.plotly_chart(fig_deaths)

st.subheader('Histogram Population')
st.plotly_chart(fig_population)

# Meita : Menampilkan pilihan opsi
option = st.selectbox('Choose an option for Line Chart', ('Total Cases', 'Total Deaths', 'Population'))

# Meita : Membuat grafik garis berdasarkan opsi yang dipilih
if option == 'Total Cases':
    fig_line = px.line(data, x='date', y='total_cases', color='iso_code',
                       title='Total Cases per Country Over Time',
                       labels={'total_cases': 'Total Cases', 'date': 'Date'})
elif option == 'Total Deaths':
    fig_line = px.line(data, x='date', y='total_deaths', color='iso_code',
                       title='Total Deaths per Country Over Time',
                       labels={'total_deaths': 'Total Deaths', 'date': 'Date'})
else:
    fig_line = px.line(data, x='date', y='population', color='iso_code',
                       title='Population per Country Over Time',
                       labels={'population': 'Population', 'date': 'Date'})
st.plotly_chart(fig_line)

# Menampilkan pilihan negara di dropdown
available_countries = data['location'].unique()
selected_country = st.selectbox('Pilih Negara', available_countries)

# Filter data berdasarkan negara yang dipilih
filtered_data = data[data['location'] == selected_country]

# Menghitung total kasus dan total kematian per negara
total_cases = filtered_data['total_cases'].iloc[-1]  # Mengambil data terbaru
total_deaths = filtered_data['total_deaths'].iloc[-1]  # Mengambil data terbaru

# Menampilkan hasil perbandingan
st.write(f"Total Kasus di {selected_country}: {total_cases}")
st.write(f"Total Kematian di {selected_country}: {total_deaths}")

# Membuat diagram lingkaran untuk perbandingan total kasus dan total kematian
fig = px.pie(values=[total_cases, total_deaths], names=['Total Cases', 'Total Deaths'],
             title=f"Perbandingan Total Kasus dan Total Kematian di {selected_country}")

st.plotly_chart(fig)


# Gabriella
st.divider()

st.subheader('Peta Sebaran Kasus, Kematian, dan Populasi Dunia')
st.write("""Dampak COVID-19 terhadap jumlah kasus, kematian, dan populasi dunia sangatlah luas dan kompleks. Dampak langsung dan tidak langsung pandemi ini telah menyebabkan kerugian yang sangat besar, baik secara ekonomi, sosial, maupun kesehatan. Untuk mengatasi dampak COVID-19, diperlukan upaya yang berkelanjutan dari berbagai pihak, baik pemerintah, swasta, maupun masyarakat.""")


# Menampilkan pilihan opsi
option = st.selectbox('Pilih data yang ingin ditampilkan', ('Total Kasus', 'Total Kematian', 'Populasi'))

# Membuat peta dunia berdasarkan opsi yang dipilih
if option == 'Total Kasus':
    fig_map = px.choropleth(data, locations='iso_code', color='total_cases',
                            hover_name='location', color_continuous_scale='Viridis',
                            title='Peta Sebaran Total Kasus')
elif option == 'Total Kematian':
    fig_map = px.choropleth(data, locations='iso_code', color='total_deaths',
                            hover_name='location', color_continuous_scale='Reds',
                            title='Peta Sebaran Total Kematian')
else:
    fig_map = px.choropleth(data, locations='iso_code', color='population',
                            hover_name='location', color_continuous_scale='Blues',
                            title='Peta Sebaran Populasi')

# Menampilkan peta pada Streamlit
st.plotly_chart(fig_map)

# Menampilkan opsi tanggal pada awal tahun, pertengahan, dan akhir tahun
start_date = pd.to_datetime('2020-01-01')
mid_date = pd.to_datetime('2020-05-01')
end_date = pd.to_datetime('2020-10-19')

# Filter data berdasarkan tanggal yang dipilih
filtered_data_start = data[data['date'] == start_date]
filtered_data_mid = data[data['date'] == mid_date]
filtered_data_end = data[data['date'] == end_date]

# Membuat peta dunia berdasarkan tanggal tertentu
if option == 'Total Kasus':
    fig_map_start = px.choropleth(filtered_data_start, locations='iso_code', color='total_cases',
                                  hover_name='location', color_continuous_scale='Viridis',
                                  title=f'Peta Sebaran Total Kasus pada {start_date}')
    fig_map_mid = px.choropleth(filtered_data_mid, locations='iso_code', color='total_cases',
                                 hover_name='location', color_continuous_scale='Viridis',
                                 title=f'Peta Sebaran Total Kasus pada {mid_date}')
    fig_map_end = px.choropleth(filtered_data_end, locations='iso_code', color='total_cases',
                                 hover_name='location', color_continuous_scale='Viridis',
                                 title=f'Peta Sebaran Total Kasus pada {end_date}')
# Membuat peta dunia berdasarkan tanggal tertentu untuk Total Kematian
if option == 'Total Kematian':
    fig_map_start = px.choropleth(filtered_data_start, locations='iso_code', color='total_deaths',
                                  hover_name='location', color_continuous_scale='Reds',
                                  title=f'Peta Sebaran Total Kematian pada {start_date}')
    fig_map_mid = px.choropleth(filtered_data_mid, locations='iso_code', color='total_deaths',
                                 hover_name='location', color_continuous_scale='Reds',
                                 title=f'Peta Sebaran Total Kematian pada {mid_date}')
    fig_map_end = px.choropleth(filtered_data_end, locations='iso_code', color='total_deaths',
                                 hover_name='location', color_continuous_scale='Reds',
                                 title=f'Peta Sebaran Total Kematian pada {end_date}')

# Membuat peta dunia berdasarkan tanggal tertentu untuk Populasi
elif option == 'Populasi':
    fig_map_start = px.choropleth(filtered_data_start, locations='iso_code', color='population',
                                  hover_name='location', color_continuous_scale='Blues',
                                  title=f'Peta Sebaran Populasi pada {start_date}')
    fig_map_mid = px.choropleth(filtered_data_mid, locations='iso_code', color='population',
                                 hover_name='location', color_continuous_scale='Blues',
                                 title=f'Peta Sebaran Populasi pada {mid_date}')
    fig_map_end = px.choropleth(filtered_data_end, locations='iso_code', color='population',
                                 hover_name='location', color_continuous_scale='Blues',
                                 title=f'Peta Sebaran Populasi pada {end_date}')

# Menampilkan peta pada Streamlit
st.plotly_chart(fig_map_start)
st.plotly_chart(fig_map_mid)
st.plotly_chart(fig_map_end)

st.divider()

# Kesimpulan
st.subheader('Kesimpulan')
st.image('masker.jpg', caption='COVID-19 membuat manusia memasuki era kebiasaan baru, salah satunya adalah kebutuhan terhadap pemakaian masker. (Sumber: halodoc.com)')
st.write("""Pandemi COVID-19 memicu kemerosotan ekonomi global, menyebabkan hilangnya lapangan kerja dan terganggunya rantai pasokan. Pemerintah meresponsnya dengan bantuan keuangan, dan beberapa industri berkembang pesat sementara industri lainnya menghadapi tantangan yang signifikan. Hingga detik ini, dunia masih dalam masa pemulihan pasca pandemi COVID-19.""")



