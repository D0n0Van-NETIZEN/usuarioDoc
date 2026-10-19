import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/D0n0Van-NETIZEN/Plantas/refs/heads/main/titanic%20(3).csv")

usuarioDoc_datos = st.checkbox("Mostrar el dataset completo")

if usuarioDoc_datos_datos:
  st.subheader("Vista previa del DataFrame")
  st.dataframe(df)

