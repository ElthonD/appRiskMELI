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
from PIL import Image

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

path_favicon = './img/favicon.ico'
im = Image.open(path_favicon)
st.set_page_config(
    page_title="AI27",
    page_icon= im,
    layout="wide",
)

# Title of the main page
pathLogo = './img/AI27Mercadolibre.png'
display = Image.open(pathLogo)
display = np.array(display)
col1, col2, col3 = st.columns([1,5,1])
col2.image(display, use_column_width=True)

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

#df = df[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo', 'Mes', 'Día']]

#df['Estatus'] = df['Tipo evento'].map(lambda x: 1 if x == "Consumado" else 0)

#El de abajo sirve
#st.dataframe(df.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)
#st.dataframe(df.style.applymap(lambda x: 'background-color: red' if x == "Consumado" else 'background-color: green', subset=['Tipo evento']), hide_index= True)

#st.dataframe(df['Estatus'].style.map(lambda x: 'color: red' if x == 0 else 'color: green'))
st.markdown("<h3 style='text-align: left;'>PLANNER MENSUAL</h3>", unsafe_allow_html=True)

container1 = st.container()
allb1 = st.checkbox("Seleccionar Todos", key="chk1")
if allb1:
    sorted_unique_mes = sorted(df['Mes'].unique())
    selected_mes = container1.multiselect('Mes(es):', sorted_unique_mes, sorted_unique_mes, key="Mes1")
    df_selected_mes = df[df['Mes'].isin(selected_mes)].astype(str)
else:
    sorted_unique_mes = sorted(df['Mes'].unique())
    selected_mes = container1.multiselect('Mes(es):', sorted_unique_mes, key="Mes2")
    df_selected_mes = df[df['Mes'].isin(selected_mes)].astype(str)

st.dataframe(df_selected_mes)

days = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 1]
st.dataframe(days)

c1, c2, c3, c4, c5, c6, c7 = st.columns([1,1,1,1,1,1,1])
with c1:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>1</h5>", unsafe_allow_html=True)
        day1 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 1]
        day1 = day1[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day1.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c2:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>2</h5>", unsafe_allow_html=True)
        day2 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 2]
        day2 = day2[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day2.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c3:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>3</h5>", unsafe_allow_html=True)
        day3 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 3]
        day3 = day3[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day3.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c4:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>4</h5>", unsafe_allow_html=True)
        day4 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 4]
        day4 = day4[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day3.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c5:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>5</h5>", unsafe_allow_html=True)
        day5 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 5]
        day5 = day5[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day5.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c6:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>6</h5>", unsafe_allow_html=True)
        day6 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 6]
        day6 = day6[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day6.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c7:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>7</h5>", unsafe_allow_html=True)
        day7 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 7]
        day7 = day7[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day7.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

c8, c9, c10, c11, c12, c13, c14 = st.columns([1,1,1,1,1,1,1])
with c8:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>8</h5>", unsafe_allow_html=True)
        day8 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 8]
        day8 = day8[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day8.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c9:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>9</h5>", unsafe_allow_html=True)
        day9 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 9]
        day9 = day9[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day9.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c10:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>10</h5>", unsafe_allow_html=True)
        day10 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 10]
        day10 = day10[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day10.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c11:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>11</h5>", unsafe_allow_html=True)
        day11 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 11]
        day11 = day11[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day11.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c12:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>12</h5>", unsafe_allow_html=True)
        day12 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 12]
        day12 = day12[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day12.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c13:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>13</h5>", unsafe_allow_html=True)
        day13 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 13]
        day13 = day13[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day13.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c14:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>14</h5>", unsafe_allow_html=True)
        day14 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 14]
        day14 = day14[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day14.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

c15, c16, c17, c18, c19, c20, c21 = st.columns([1,1,1,1,1,1,1])
with c15:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>15</h5>", unsafe_allow_html=True)
        day15 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 15]
        day15 = day15[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day15.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c16:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>16</h5>", unsafe_allow_html=True)
        day16 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 16]
        day16 = day16[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day16.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c17:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>17</h5>", unsafe_allow_html=True)
        day17 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 17]
        day17 = day17[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day17.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c18:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>18</h5>", unsafe_allow_html=True)
        day18 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 18]
        day18 = day18[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day18.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c19:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>19</h5>", unsafe_allow_html=True)
        day19 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 19]
        day19 = day19[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day19.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c20:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>2o</h5>", unsafe_allow_html=True)
        day20 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 20]
        day20 = day20[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day20.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c21:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>21</h5>", unsafe_allow_html=True)
        day21 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 21]
        day21 = day21[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day21.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

c22, c23, c24, c25, c26, c27, c28 = st.columns([1,1,1,1,1,1,1])
with c22:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>22</h5>", unsafe_allow_html=True)
        day22 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 22]
        day22 = day22[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day22.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c23:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>23</h5>", unsafe_allow_html=True)
        day23 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 23]
        day23 = day23[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day23.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c24:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>24</h5>", unsafe_allow_html=True)
        day24 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 24]
        day24 = day24[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day24.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c25:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>25</h5>", unsafe_allow_html=True)
        day25 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 25]
        day25 = day25[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day25.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c26:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>26</h5>", unsafe_allow_html=True)
        day26 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 26]
        day26 = day26[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day26.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c27:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>27</h5>", unsafe_allow_html=True)
        day27 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 27]
        day27 = day27[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day27.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c28:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>28</h5>", unsafe_allow_html=True)
        day28 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 28]
        day28 = day28[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day28.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

c29, c30, c31, c32, c33, c34, c35 = st.columns([1,1,1,1,1,1,1])
with c29:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>29</h5>", unsafe_allow_html=True)
        day29 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 29]
        day29 = day29[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day29.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c30:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>30</h5>", unsafe_allow_html=True)
        day30 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 30]
        day30 = day30[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day30.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c31:
    with st.container(border=True):
        st.markdown("<h5 style='text-align: left;'>31</h5>", unsafe_allow_html=True)
        day31 = df_selected_mes.loc[df_selected_mes.loc[:, 'Día'] == 31]
        day31 = day31[['Año', 'Tipo evento', 'Estado', 'Tramo']]
        st.dataframe(day31.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

        #day31 = df_selected_mes.groupby(by=['Día'])
        #d31 = day31.apply(lambda x: x[x['Día'] == 31])
        #d31 = d31[['Año', 'Tipo evento', 'Fecha y Hora', 'Estado', 'Tramo']]
        #st.dataframe(d31.style.applymap(lambda x: 'color: red' if x == "Consumado" else 'color: green', subset=['Tipo evento']), hide_index= True)

with c32:
    st.container(border=None)

with c33:
    st.container(border=None)

with c34:
    st.container(border=None)

with c35:
    st.container(border=None)