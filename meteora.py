# Top pools mostrando el bin step
# Introduce tu posicion y te avisamos con la rentabilidad
# Introduce tu wallet
# Introdce una address/pair y te decimos la mas rentable

import streamlit as st
import requests
import pandas as pd

# Función para filtrar el DataFrame
def filter_dataframe(df, query):
    return df.query(query)

# URL de la API
url = "https://dlmm-api.meteora.ag/pair/all"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Seleccionar solo las columnas necesarias
    df = df[['address', 'pair', 'bin_step', 'apr', 'apy', 'liquidity', 'base_fee_percentage']]

    # Filtros
    st.sidebar.title("Filtros")
    address = st.sidebar.text_input("Dirección (Address):")
    name = st.sidebar.text_input("Nombre (Name):")
    liquidity_min = st.sidebar.number_input("Liquidez Mínima (Liquidity Min):", min_value=0.0)
    liquidity_max = st.sidebar.number_input("Liquidez Máxima (Liquidity Max):", min_value=0.0, value=1e20)
    apr_min = st.sidebar.number_input("APR Mínimo (APR Min):", min_value=0.0)
    apr_max = st.sidebar.number_input("APR Máximo (APR Max):", min_value=0.0, value=1e20)

    # Convertir los valores de liquidez y APR a números flotantes
    df['liquidity'] = df['liquidity'].astype(float)
    df['apr'] = df['apr'].astype(float)

    # Aplicar filtros
    query = f"address.str.contains('{address}') & pair.str.contains('{name}') & liquidity >= {liquidity_min} & liquidity <= {liquidity_max} & apr >= {apr_min} & apr <= {apr_max}"
    filtered_df = filter_dataframe(df, query)

    # Mostrar resultados
    if not filtered_df.empty:
        st.write(filtered_df)
    else:
        st.write("No se encontraron resultados que cumplan con los filtros.")
else:
    st.write("Error al obtener datos de la API.")
