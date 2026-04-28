# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # DS 7: Energía asequible y no contaminante  ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto de la velocidad del viento 
en la efucincia de un motor eolico, alineado con el **DS 7: Energía asequible y no contaminante**.
""")
# Insertamos una imagen
st.image("ods7.png", caption="Impacto del viento en la eficincia.")



# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetros del viento")

temp_input = st.sidebar.slider("velocidad del viento", 0, 70, 35)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('Energia_eolica_ODS7.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['Velocidad_Viento_ms']]
y = df['Eficiencia_Energetica_kWh']

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

# Presentamos loa resultados
st.subheader('Eficiencia ')
st.write(f'produccion en KW: {prediccion:.2f}')

if prediccion < 100:
        st.success("poca produccion ")
elif prediccion < 1000:
        st.warning("produccion buena")
else:
        st.error("Exelente ")
