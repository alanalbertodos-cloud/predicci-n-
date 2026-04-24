
import numpy as np
import streamlit as st
import pandas as pd

# Título
st.write("# ODS 2: Hambre Cero")

# Descripción
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir
la cantidad de calorías consumidas en función del ingreso mensual.

Está alineada con el **ODS 2: Hambre Cero**, que busca combatir la desnutrición
y mejorar el acceso a alimentos.
""")

# Imagen (puedes poner una relacionada)
st.image("foto.jpg",
caption="Relación entre ingreso mensual y consumo calórico")

# Sidebar
st.sidebar.header("Parámetros")

# Usuario ingresa ingreso mensual
ingreso_input = st.sidebar.slider(
"Ingreso mensual ($)",
2500,
20000,
6000
)

# Cargar datos
df = pd.read_csv("datos_hambre_cero.csv")

# Variables
X = df[['Ingreso_Mensual']]
y = df['Calorias_Consumidas']

# Modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
X,y,test_size=0.30,random_state=0
)

modelo = LinearRegression()
modelo.fit(X_train,y_train)

# Predicción
b1 = modelo.coef_
b0 = modelo.intercept_

prediccion = b0 + b1[0]*ingreso_input

# Resultado
st.subheader("Predicción nutricional")
st.write(
f"Calorías consumidas estimadas: {prediccion:.2f} kcal"
)

# Clasificación
if prediccion < 2000:
    st.error("Nivel insuficiente de consumo calórico")
elif prediccion < 2500:
    st.warning("Nivel aceptable pero mejorable")
else:
    st.success("Nivel adecuado de consumo calórico")
