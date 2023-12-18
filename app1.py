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

b1 = st.columns(1)

with b1:
    container1 = st.container()
    allb1 = st.checkbox("Seleccionar Todos", key="chk1")
    if allb1:
        sorted_unique_mes = sorted(df['EstadoOrigen'].unique())
        selected_mes = container1.multiselect('Origen(es):', sorted_unique_mes, sorted_unique_mes, key="Mes1")
        df_selected_mes = df[df['EstadoOrigen'].isin(selected_mes)].astype(str)
    else:
        sorted_unique_mes = sorted(df['EstadoOrigen'].unique())
        selected_mes = container1.multiselect('Origen(es)', sorted_unique_mes, key="Mes1")
        df_selected_mes = df[df['EstadoOrigen'].isin(selected_mes)].astype(str)

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

c15, c16, c17, c18, c19, c20, c21 = st.columns([1,1,1,1,1,1,1])
with c15:
    with st.container(border=True):
        st.header("15")
        day15 = df.groupby(by=['Día'])
        d15 = day15.apply(lambda x: x[x['Día'] == 15])
        d15 = d15[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d15.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c16:
    with st.container(border=True):
        st.header("16")
        day16 = df.groupby(by=['Día'])
        d16 = day16.apply(lambda x: x[x['Día'] == 16])
        d16 = d16[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d16.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c17:
    with st.container(border=True):
        st.header("17")
        day17 = df.groupby(by=['Día'])
        d17 = day10.apply(lambda x: x[x['Día'] == 17])
        d17 = d17[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d17.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c18:
    with st.container(border=True):
        st.header("18")
        day18 = df.groupby(by=['Día'])
        d18 = day18.apply(lambda x: x[x['Día'] == 18])
        d18 = d18[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d18.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c19:
    with st.container(border=True):
        st.header("19")
        day19 = df.groupby(by=['Día'])
        d19 = day19.apply(lambda x: x[x['Día'] == 19])
        d19 = d19[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d19.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c20:
    with st.container(border=True):
        st.header("20")
        day20 = df.groupby(by=['Día'])
        d20 = day20.apply(lambda x: x[x['Día'] == 20])
        d20 = d20[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d20.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c21:
    with st.container(border=True):
        st.header("21")
        day21 = df.groupby(by=['Día'])
        d21 = day21.apply(lambda x: x[x['Día'] == 21])
        d21 = d21[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d21.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)


c22, c23, c24, c25, c26, c27, c28 = st.columns([1,1,1,1,1,1,1])
with c22:
    with st.container(border=True):
        st.header("22")
        day22 = df.groupby(by=['Día'])
        d22 = day22.apply(lambda x: x[x['Día'] == 22])
        d22 = d22[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d22.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c23:
    with st.container(border=True):
        st.header("23")
        day23 = df.groupby(by=['Día'])
        d23 = day23.apply(lambda x: x[x['Día'] == 23])
        d23 = d23[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d23.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c24:
    with st.container(border=True):
        st.header("24")
        day24 = df.groupby(by=['Día'])
        d24 = day24.apply(lambda x: x[x['Día'] == 24])
        d24 = d24[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d24.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c25:
    with st.container(border=True):
        st.header("25")
        day25 = df.groupby(by=['Día'])
        d25 = day18.apply(lambda x: x[x['Día'] == 25])
        d25 = d25[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d25.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c26:
    with st.container(border=True):
        st.header("26")
        day26 = df.groupby(by=['Día'])
        d26 = day26.apply(lambda x: x[x['Día'] == 26])
        d26 = d26[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d26.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c27:
    with st.container(border=True):
        st.header("27")
        day27 = df.groupby(by=['Día'])
        d27 = day27.apply(lambda x: x[x['Día'] == 27])
        d27 = d27[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d27.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c28:
    with st.container(border=True):
        st.header("28")
        day28 = df.groupby(by=['Día'])
        d28 = day28.apply(lambda x: x[x['Día'] == 28])
        d28 = d28[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d28.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

c29, c30, c31, c32, c33, c34, c35 = st.columns([1,1,1,1,1,1,1])
with c29:
    with st.container(border=True):
        st.header("29")
        day29 = df.groupby(by=['Día'])
        d29 = day29.apply(lambda x: x[x['Día'] == 29])
        d29 = d29[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d29.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c30:
    with st.container(border=True):
        st.header("30")
        day30 = df.groupby(by=['Día'])
        d30 = day30.apply(lambda x: x[x['Día'] == 22])
        d30 = d30[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d30.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)
with c31:
    with st.container(border=True):
        st.header("31")
        day31 = df.groupby(by=['Día'])
        d31 = day31.apply(lambda x: x[x['Día'] == 31])
        d31 = d31[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        st.dataframe(d31.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c32:
    st.container(border=None)

with c33:
    st.container(border=None)

with c34:
    st.container(border=None)

with c35:
    st.container(border=None)