import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple
import matplotlib.pyplot as plt


st.title("Historial de produccion del campo Volve")

st.write("---")
st.markdown("""El campo volve es un campo Offshore que tuvo una produccion aproximada de
            8 años empezando desde el año 2008 hasta el año 2016""")
st.write("---")

ima1= Image.open("Recursos/2623836.png")
st.image(ima1, width=100, use_column_width=True)

#Creamos el menu

st.sidebar.title("⬇ Menu")
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "tv-fill", "box"],)

# Carga de archivos

file = st.sidebar.file_uploader("Sube tu archivo")
def data(dataframe):
    st.subheader("**View dataframe**")
    st.write(dataframe.head())
    st.subheader("**Statistical summary**")
    st.write(dataframe.describe())
if file:
    df = pd.read_excel(file)
    df1 = pd.DataFrame(df)
    if options == "Data":
        data(df)

