# Top pools mostrando el bin step
# Introduce tu posicion y te avisamos con la rentabilidad
# Introduce tu wallet
# Introdce una address/pair y te decimos la mas rentable


import streamlit as st
import requests
import pandas as pd

# URL de la API
url = "https://dlmm-api.meteora.ag/pair/all"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.write("Error al obtener datos de la API.")
