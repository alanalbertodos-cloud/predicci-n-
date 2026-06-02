
import numpy as np
import streamlit as st
import pandas as pd

# Título
st.write("# Optimización y Modelado de Recursos Educativos (ODS 4)")

# Descripción
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir
el Porcentaje de termino en función de la Inversión por estudiante.

Está alineada con el **ODS 4: Educación de Calidad**, que busca educación inclusiva, equitativa y de calidad.
""")

# Imagen (puedes poner una relacionada)
st.image("ods4.jpg",
caption="Relación entre porcentaje de termino e inversión por estudiante")

# Sidebar
st.sidebar.header("Parámetros")

# Usuario ingresa ingreso mensual
ingreso_input = st.sidebar.slider(
"inversión por estudiante(USD R)",
2500,
17838,
6000
)

# Cargar datos
df = pd.read_csv("datosl_final.csv")

# Variables
X = df[['Inversión por estudiante']]
y = df['Porcentaje de termino']

# Modelo

from sklearn.linear_model import LinearRegression



modelo = LinearRegression()
modelo.fit(X,y)

# Predicción
b1 = modelo.coef_
b0 = modelo.intercept_

prediccion = b0 + b1[0]*ingreso_input

# Resultado
st.subheader("Predicción del Porcentaje de Termino")
st.write(
f"Porcentaje de termino estimado: {prediccion:.2f}%"
)

