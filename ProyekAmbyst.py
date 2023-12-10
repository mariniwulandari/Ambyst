import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visualisasi Data Covid-19")
st.write("oleh Kelompok Ambyst")

df = pd.read_csv('raw_data.csv')
#df = pd.read_csv('raw_data.csv')


st.write("## 5 data pertama")
st.write( df.head() )

st.write("## Info Data")
st.write( df.describe() )

# Load data dari CSV
file_path = "raw_data.csv"  # Menggunakan nama file "raw_data.csv"
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