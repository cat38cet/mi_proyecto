
import streamlit as st
import pandas as pd
import altair as alt
import requests

st.title('Visualización de Datos con Streamlit y Flask')

# Obtener los datos desde el servidor Flask
response = requests.get('http://localhost:5000/data')
data = response.json()

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar los datos
st.write(df)

# Crear un gráfico de barras con Altair
chart = alt.Chart(df).mark_bar().encode(
    x='Column 1:N',
    y='Column 2:Q'
)

# Mostrar el gráfico en la aplicación de Streamlit
st.altair_chart(chart, use_container_width=True)
