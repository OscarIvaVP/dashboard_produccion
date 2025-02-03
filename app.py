import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard de Producción Agrícola", layout="wide")

# Título
st.title("📊 Dashboard de Producción Agrícola")

# Generación de datos simulados
np.random.seed(42)
años = np.arange(2015, 2025)
producción = np.random.randint(500, 3000, size=len(años))
rendimiento = np.random.uniform(1.5, 4.5, size=len(años))
costos = np.random.randint(100, 1000, size=len(años))
cultivos = np.random.choice(["Maíz", "Arroz", "Trigo", "Café"], size=len(años))

df = pd.DataFrame({
    "Año": años,
    "Producción (Ton)": producción,
    "Rendimiento (Ton/ha)": rendimiento,
    "Costos ($/ha)": costos,
    "Cultivo": cultivos
})

# Filtro por año
año_seleccionado = st.sidebar.selectbox("Selecciona un Año:", años)
df_filtrado = df[df["Año"] == año_seleccionado]

# ---- SECCIÓN 1: Gráficos con variables numéricas ----
st.subheader("📈 Análisis Numérico")

col1, col2, col3 = st.columns(3)

# 1️⃣ Gráfico de dispersión
with col1:
    st.markdown("**Gráfico de Dispersión: Producción vs Costos**")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df["Producción (Ton)"], y=df["Costos ($/ha)"], hue=df["Año"], palette="coolwarm", ax=ax)
    st.pyplot(fig)

# 2️⃣ Gráfico de líneas
with col2:
    st.markdown("**Gráfico de Líneas: Producción a lo largo del tiempo**")
    fig, ax = plt.subplots()
    sns.lineplot(x=df["Año"], y=df["Producción (Ton)"], marker="o", ax=ax)
    st.pyplot(fig)

# 3️⃣ Boxplot de costos
with col3:
    st.markdown("**Boxplot de Costos ($/ha)**")
    fig, ax = plt.subplots()
    sns.boxplot(y=df["Costos ($/ha)"], ax=ax)
    st.pyplot(fig)

# ---- SECCIÓN 2: Gráficos con variables categóricas ----
st.subheader("📊 Análisis Categórico")

col4, col5 = st.columns(2)

# 4️⃣ Gráfico de barras (Producción por Cultivo)
with col4:
    st.markdown("**Producción por Tipo de Cultivo**")
    fig, ax = plt.subplots()
    sns.barplot(x=df["Cultivo"], y=df["Producción (Ton)"], estimator=np.sum, ci=None, palette="viridis", ax=ax)
    st.pyplot(fig)

# 5️⃣ Gráfico de sectores (Pie Chart)
with col5:
    st.markdown("**Distribución de Cultivos**")
    fig, ax = plt.subplots()
    df_cultivos = df["Cultivo"].value_counts()
    ax.pie(df_cultivos, labels=df_cultivos.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
    st.pyplot(fig)

# Mostrar la tabla de datos filtrada
st.subheader(f"📋 Datos para el Año {año_seleccionado}")
st.dataframe(df_filtrado)
