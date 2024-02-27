import streamlit as st
import pandas as pd
import numpy as np

st.title("Viagens Uber NYC")

DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis=1, inplace=True)
    data["date/time"] = pd.to_datetime(data["date/time"])
    return data

# Carregando os dados
data_load_state = st.text("Carregando dados...")
data = load_data(10000)
data_load_state.text("Carregamento dos dados foi realizado!")

# Exibindo os dados em uma tabela
if st.checkbox("Mostrar tabela com os dados"):
    st.write(data)

# Exibindo um gráfica de barras
st.subheader("Número de viagens por hora")
hist_values = np.histogram(data["date/time"].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Exibindo o mapa de viagens
hour_to_filter = st.slider("Hora", 0, 23, 12)
st.subheader(f"Mapa com todas as viagens realizadas em {hour_to_filter}:00.")
filtered_data = data[data["date/time"].dt.hour == hour_to_filter]
st.map(filtered_data)


    