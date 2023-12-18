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


st.set_page_config(
    page_title="AI27",
    page_icon="🧊",
    layout="wide",
)
    
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

#df['Estatus'] = df['Tipo evento'].map(lambda x: 1 if x == "Consumado" else 0)

#El de abajo sirve
#st.dataframe(df.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)
#st.dataframe(df.style.applymap(lambda x: 'background-color: red' if x == "Consumado" else 'background-color: green', subset=['Tipo evento']), hide_index= True)

#st.dataframe(df['Estatus'].style.map(lambda x: 'color: red' if x == 0 else 'color: green'))

c1, c2, c3, c4, c5, c6, c7 = st.columns([1,1,1,1,1,1,1])
with c1:
    with st.container(border=True):
        st.header("1")
        day1 = df.groupby(by=['Día'])
        d1 = day1.apply(lambda x: x[x['Día'] == 1])
        d1 = d1[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d1.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c2:
    with st.container(border=True):
        st.header("2")
        day2 = df.groupby(by=['Día'])
        d2 = day2.apply(lambda x: x[x['Día'] == 2])
        d2 = d2[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d2.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c3:
    with st.container(border=True):
        st.header("3")
        day3 = df.groupby(by=['Día'])
        d3 = day3.apply(lambda x: x[x['Día'] == 3])
        d3 = d3[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d3.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c4:
    with st.container(border=True):
        st.header("4")
        day4 = df.groupby(by=['Día'])
        d4 = day4.apply(lambda x: x[x['Día'] == 4])
        d4 = d4[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d4.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c5:
    with st.container(border=True):
        st.header("5")
        day5 = df.groupby(by=['Día'])
        d5 = day5.apply(lambda x: x[x['Día'] == 5])
        d5 = d5[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d5.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c6:
    with st.container(border=True):
        st.header("6")
        day6 = df.groupby(by=['Día'])
        d6 = day6.apply(lambda x: x[x['Día'] == 6])
        d6 = d6[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d6.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c7:
    with st.container(border=True):
        st.header("7")
        day7 = df.groupby(by=['Día'])
        d7 = day7.apply(lambda x: x[x['Día'] == 7])
        d7 = d7[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d7.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)
c8, c9, c10, c11, c12, c13, c14 = st.columns([1,1,1,1,1,1,1])
with c8:
    with st.container(border=True):
        st.header("8")
        day8 = df.groupby(by=['Día'])
        d8 = day8.apply(lambda x: x[x['Día'] == 8])
        d8 = d8[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d8.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c9:
    with st.container(border=True):
        st.header("9")
        day9 = df.groupby(by=['Día'])
        d9 = day9.apply(lambda x: x[x['Día'] == 9])
        d9 = d9[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d9.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c10:
    with st.container(border=True):
        st.header("10")
        day10 = df.groupby(by=['Día'])
        d10 = day10.apply(lambda x: x[x['Día'] == 10])
        d10 = d10[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d10.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c11:
    with st.container(border=True):
        st.header("11")
        day11 = df.groupby(by=['Día'])
        d11 = day11.apply(lambda x: x[x['Día'] == 11])
        d11 = d11[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d11.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c12:
    with st.container(border=True):
        st.header("12")
        day12 = df.groupby(by=['Día'])
        d12 = day12.apply(lambda x: x[x['Día'] == 12])
        d12 = d12[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d12.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c13:
    with st.container(border=True):
        st.header("13")
        day13 = df.groupby(by=['Día'])
        d13 = day13.apply(lambda x: x[x['Día'] == 13])
        d13 = d13[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d13.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c14:
    with st.container(border=True):
        st.header("14")
        day14 = df.groupby(by=['Día'])
        d14 = day14.apply(lambda x: x[x['Día'] == 14])
        d14 = d14[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d14.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)


