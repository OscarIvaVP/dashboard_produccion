import streamlit as st
import pandas as pd

# Título del dashboard
st.title("Dashboard de Producción Agrícola")

# Cargar datos de ejemplo
data = {'Año': [2020, 2021, 2022],
        'Producción (Ton)': [1000, 1500, 1800]}
df = pd.DataFrame(data)

# Mostrar datos en tabla
st.write("Datos de Producción:")
st.dataframe(df)

# Gráfico
st.line_chart(df.set_index("Año"))

