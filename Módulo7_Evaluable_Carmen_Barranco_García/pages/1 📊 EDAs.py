import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = sns.load_dataset('diamonds').dropna()
st.title('Gráficos de Streamlit sobre Dataset Diamonds')

@st.cache_data
def load_tips_data():
    return sns.load_dataset('diamonds')

col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Volver a Inicio'):
        st.switch_page('app.py')
        
with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🤖 Regresión.py')
        
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 🤖 Clasificación.py')

st.header('1. DataFrame Diamonds')
df = load_tips_data()
st.dataframe(df, use_container_width=True)

# Filtros
st.header('Filtros globales')
st.subheader('Filtros categóricos')

# Filtro  por corte
cut = df['cut'].unique().tolist()
selected_cut = st.multiselect('Selecciona los tipos de corte.', options=cut, default=cut)

# Filtro por color 
color = df['color'].unique().tolist()
selected_color = st.multiselect('Selecciona los tipos de color.', options=color, default=color)

# Filtro por claridad 
clarity = df['clarity'].unique().tolist()
selected_clarity = st.multiselect('Selecciona los tipos de claridad.', options=clarity, default=clarity)

# Obtenemos mínimo y máximo columna price
price_min, price_max = st.slider(
    'Selecciona rango de Precio', 
    min_value=df['price'].min(),
    max_value=df['price'].max(),
    value=(df['price'].min(), df['price'].max())
)

# Obtenemos mínimo y máximo columna carat
carat_min, carat_max = st.slider(
    'Selecciona rango de Quilate', 
    min_value=df['carat'].min(),
    max_value=df['carat'].max(),
    value=(df['carat'].min(), df['carat'].max())
)

# Obtenemos mínimo y máximo columna depth
depth_min, depth_max = st.slider(
    'Selecciona rango de Profundidad', 
    min_value=df['depth'].min(),
    max_value=df['depth'].max(),
    value=(df['depth'].min(), df['depth'].max())
)

# Obtenemos mínimo y máximo columna table
table_min, table_max = st.slider(
    'Selecciona rango de Table', 
    min_value=df['table'].min(),
    max_value=df['table'].max(),
    value=(df['table'].min(), df['table'].max())
)

# Aplicar los filtros
df_filtered = df[
    (df['cut'].isin(selected_cut)) & 
    (df['color'].isin(selected_color)) &
    (df['clarity'].isin(selected_clarity)) &
    (df['price'] >= price_min) & (df['price'] <= price_max) &
    (df['carat'] >= carat_min) & (df['carat'] <= carat_max) &
    (df['depth'] >= depth_min) & (df['depth'] <= depth_max) &
    (df['table'] >= table_min) & (df['table'] <= table_max)
]

st.table(df_filtered.head())
st.write(f'Nº filas antes de filtrar: **{df.shape[0]}**')
st.write(f'Nº filas después de filtrar: **{df_filtered.shape[0]}**')
st.write(f'Nº filas eliminadas por filtro: **{df.shape[0] - df_filtered.shape[0]}**')



st.header('2. Gráficos univariantes')

fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df_filtered['price'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma sobre columna precio')
ax.set_xlabel('Precio')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(6,4))
sns.kdeplot(df_filtered, x='table')
sns.rugplot(df_filtered, x='table')
sns.histplot(df_filtered, x='table', kde=True)
ax.set_title('Análisis univariante de table')
ax.set_xlabel('Table')
st.pyplot(fig)


st.header('3. Gráficos bivariantes')

fig, ax = plt.subplots(figsize=(6,4))
ax.boxplot(df_filtered['depth'], showmeans=True)
ax.set_title('Boxplot de Profundidad')
ax.set_xlabel('Profundidad')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df_filtered, x='carat', y='price')
ax.set_title('Relación entre precio y quilates')
ax.set_xlabel('Quilates')
ax.set_ylabel('Precio')
ax.legend()
ax.grid()

st.header('4. Gráficos multivariantes')

fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(df_filtered.corr(numeric_only=True).round(2), annot=True, cmap='viridis')
ax.set_title('Correlaciones')
st.pyplot(fig)

st.header('Descargar datos')
st.html('<p style="text-align:center">Descarga el dataset original o con los filtros actuales</p>')
