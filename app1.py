### Librerías

import streamlit as st
import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMapWithTime
from streamlit_folium import folium_static
from dateutil.relativedelta import *
import seaborn as sns; sns.set_theme()
import numpy as np
import requests

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')


    
@st.cache_data(show_spinner='Cargando Datos... Espere...', persist=True)
def load_HR():

    rutaA = r'./data/Historico de Robos MELI.xlsx'
    Robos = pd.read_excel(rutaA, sheet_name = "Data")
    Robos = Robos.drop(['Operadores','CM', 'Línea Reacción'], axis=1)
    Robos['Fecha'] = Robos['Fecha'].dt.strftime('%m/%d/%Y')
    Robos['Fecha'] = pd.to_datetime(Robos['Fecha'], format="%Y/%m/%d", infer_datetime_format=True)
    Robos['Año'] = Robos.Fecha.apply(lambda x: x.year)
    Robos['MesN'] = Robos['Fecha'].apply(lambda x: x.month)
    Robos['Mes'] = Robos['MesN'].map({1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"})
    Robos['Dia'] = Robos.Fecha.apply(lambda x: x.day)
    Robos['Fecha y Hora'] = pd.to_datetime(Robos['Fecha y Hora'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    Robos = Robos.dropna()

    return Robos


df = load_HR()

df = df[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo', 'Mes', 'Día']]

df['Estatus'] = df['Tipo evento'].map(lambda x: 1 if x == "Consumado" else 0)

st.dataframe(df.style.applymap(lambda x: 'color: red' if any('Consumado' in words for words in x.split()) else 'color: green'))


#st.dataframe(df['Estatus'].style.map(lambda x: 'color: red' if x == 0 else 'color: green'))


def _color_red_or_green(val):
    color = 'red' if val == 0 else 'green'
    return f'background-color: {color}'

def color_survived(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

df.style.applymap(_color_red_or_green)

st.dataframe(df)

"""
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1:
        st.header("1")
        st.dataframe(df)

    with c2:
        st.header("2")
        st.dataframe(df)

    with c3:
        st.header("3")
        st.dataframe(df)

    with c4:
        st.header("4")
        st.dataframe(df)

    with c5:
        st.header("5")
        st.dataframe(df)

    with c6:
        st.header("6")
        st.dataframe(df)

    with c7:
        st.header("7")
        st.dataframe(df)
"""

