import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data(nrows=18316):
    return pd.read_csv("https://raw.githubusercontent.com/D0n0Van-NETIZEN/usuarioDoc/refs/heads/main/global_suicide_rates_real_who_worldbank.csv",nrows=nrows,encoding="latin-1")

usuarioDoc = load_data()

st.header("global suicide rates")

if st.sidebar.checkbox("Mostrar todos los datos"):
    st.subheader("Todos los datos")
    st.write(f"Total de paises: {len(usuarioDoc)}")
    st.dataframe(usuarioDoc)

def filtrar_por_suicidios(df, texto):
    return df[df["suicide_rate_per_100k"].str.contains(texto, case=False, na=False, regex=False)]

titulo = st.sidebar.text_input("total_country_popular:")
if st.sidebar.button("Buscar por pais"):
    resultado = filtrar_por_posicion(usuarioDoc, titulo)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de asesinatos: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_(df, texto):
    return df[df["club_name"].str.contains(texto, case=False, na=False, regex=False)]

country = st.sidebar.text_input("Pais:")
if st.sidebar.button("Buscar por club"):
    resultado = filtrar_por_pais(usuarioDoc, pais)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de paises: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_pais(df, texto):
    return df[df["pais"].astype(str) == texto]

edad = st.sidebar.text_input("Edad del jugador:")
if st.sidebar.button("Buscar por edad"):
    resultado = filtrar_por_edad(FC26_data, edad)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_liga(df, liga):
    return df[df["league_name"] == liga]

ligas = sorted(FC26_data["league_name"].dropna().unique())
liga = st.sidebar.selectbox("Liga:", ligas)
if st.sidebar.button("Buscar por liga"):
    resultado = filtrar_por_liga(FC26_data, liga)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado) 

def filtrar_por_calificacion(df, minimo, maximo):
    return df[(df["overall"] >= minimo) & (df["overall"] <= maximo)]

cal_min, cal_max = st.sidebar.slider("Calificación global:", 57, 91, (57, 91))
if st.sidebar.button("Buscar por calificación"):
    resultado = filtrar_por_calificacion(FC26_data, cal_min, cal_max)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)   

fig, ax = plt.subplots()
ax.hist(FC26_data["overall"], bins=20)
ax.set_xlabel("Calificación global")
ax.set_ylabel("Cantidad de jugadores")
st.header("Cantidad de jugadores y su  calificación global")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
top10 = FC26_data.nlargest(10, "overall")
y_pos = top10['short_name']
x_pos = top10['overall']
ax2.barh(y_pos, x_pos)
ax2.invert_yaxis()   # el mejor queda arriba
ax2.set_ylabel("Jugador")
ax2.set_xlabel("Calificación global")
ax2.set_title("Calificación global de 10 jugadores")
st.header("Top 10 jugadores")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(FC26_data.age, FC26_data.potential)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Potencial")
st.header("Edad y Potencial")
st.pyplot(fig3)


st.title("Donovan Gonzalez Sanchez")
st.header("Matrícula: S26004675")
st.header("Mapa aquí abajo 👇")

map_data = pd.DataFrame(
  np.random.randn(1, 2) / [500, 500] + [18.8033, -97.1808],
  columns=['lat', 'lon'])

st.title("Fortin de las Flores, Ver.")
st.header("Fortin")
st.header("CP: 94470")

st.map(map_data)