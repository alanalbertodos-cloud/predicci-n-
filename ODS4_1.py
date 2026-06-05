
import numpy as np
import streamlit as st
import pandas as pd

# Título
st.write("# Optimización y Modelado de Recursos Educativos (ODS 4)")

# Descripción
st.markdown("""
Esta aplicación utiliza **Machine Learning** para la optimizacion de recursos  en **Bulgaria**.

Está alineada con el **ODS 4: Educación de Calidad**, que busca educación inclusiva, equitativa y de calidad.
""")

# Imagen (puedes poner una relacionada)
st.image("ods4.jpg",
caption="Relación entre porcentaje de termino e inversión por estudiante")

# Sidebar
st.sidebar.header("Parámetros")

# Usuario ingresa ingreso mensual
# Usaremos un deslizador
st.sidebar.header("Presupuesto")
# Definimos los parámetros de nuestro deslizador:

presupuesto = st.sidebar.slider("Presupuesto",1400000000, 6000000000,
3000000000)
st.sidebar.header("Porcentaje de Becas")
porcentaje_becas = st.sidebar.slider("Porcentaje de Becas", 0.0, 1.0, 0.2)
st.sidebar.header("Porcentaje de Infraestructura")
porcentaje_infra = st.sidebar.slider("Porcentaje de Infraestructura", 0.0, 1.0,0.5)
st.sidebar.header("Porcentaje de Docentes")
porcentaje_docentes = st.sidebar.slider("Porcentaje de Docentes", 0.0, 1.0, 0.15)

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

# Especificamos datos por población
numero = 713546
prep_alumno = presupuesto/numero

# Calculamos el presupuesto asignado a cada rubro
presupuesto_becas = presupuesto * porcentaje_becas
presupuesto_infra = presupuesto * porcentaje_infra
presupuesto_docentes = presupuesto * porcentaje_docentes

# Presentamos loa resultados
total_gastado = presupuesto*(porcentaje_becas + porcentaje_infra +
porcentaje_docentes)


# Validar restricciones
import warnings
if total_gastado != presupuesto:
  st.error("El total gastado debe ser exactamente igual al presupuesto.")
elif presupuesto_becas < presupuesto*.20:
  st.warning("El presupuesto de becas no cumple con el mínimo del 20%.",UserWarning)
elif presupuesto_infra > presupuesto*.50:
  st.warning("El presupuesto de infraestructura excede el tope del 50%.",UserWarning)
elif presupuesto_docentes < presupuesto*.15:
  st.warning("La capacitación docente está por debajo del 15% obligatorio.",UserWarning)
else:
  st.success("Combinación de presupuesto válida.")


st.subheader('Impacto alcanzado')
impacto = b0 + prep_alumno*b1[0] + presupuesto_infra/100000000*0.15 +
presupuesto_docentes/100000000*.14
st.metric("Impacto Proyectado ODS 4", f"+{float(impacto):.3f}%")
# Presentamos el tipo de filosofía
if porcentaje_becas >= 0.40:
  filosofia = "Bienestar Primero (Equidad y Movilidad Social)"
elif porcentaje_infra >= 0.45:
  filosofia = "Rendimiento Estructural (Desarrollo Sostenible)"
elif porcentaje_docentes >= 0.35:
  filosofia = "Efecto Multiplicador (Excelencia Académica)"
else:
  filosofia = "Gobernanza Equilibrada (Modelo Balanceado)"

st.subheader("Clasificación Estratégica del Modelo")
st.info(f"Su propuesta óptima califica como un enfoque de: **{filosofia}**")
