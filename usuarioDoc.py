import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names_link = 
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.dataframe(names_data)
