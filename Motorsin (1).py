# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía asequible y no contaminante  ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto de la radiacion solar
en la eficiencia de un panel solar, alineado con el **DS 7: Energía asequible y no contaminante**.
""")
# Insertamos una imagen
st.image("istockphoto-1337173750-612x612.jpg", caption="Impacto del viento en la eficincia.")



# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetros del intencidad")

temp_input = st.sidebar.slider("Intensidad del sol (W/m²)", 204.0, 1050.0, 625.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ODS7_limpiio.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['VAR_2']]
y = df['VAR_4']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la velocidad seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos los resultados
st.subheader('Eficiencia y Resultados')
st.write(f'Producción estimada: **{prediccion:.2f} KW**')
if prediccion < 45.0:
    st.error("Poca producción: Niveles críticos de energía.")
elif prediccion < 85.0:
    st.warning("Producción buena: Operación dentro de parámetros normales.")
else:
    st.success("Excelente producción: Máximo rendimiento del panel.")
