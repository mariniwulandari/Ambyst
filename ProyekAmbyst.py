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