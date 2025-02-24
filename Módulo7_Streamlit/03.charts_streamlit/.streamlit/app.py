import streamlit as st
import seaborn as sns
import pandas as pd   
import numpy as np 

# Charts gráficos nativos streamlit
st.title('Graficos nativos de Streamlit')

# 1. bar_chart
st.header('Gráfica de barras: st.bar_chart')
df_tips = sns.load_dataset('tips')
df_group_by_day = df_tips.groupby('day', observed=True)['total_bill'].sum()
st.table(df_group_by_day)
st.bar_chart(df_group_by_day)

# 2. line_chart
st.header('Gráfica de líneas: st.line_chart')
df_flights = sns.load_dataset('flights')
st.table(df_flights.head())


df_pivot = df_flights.pivot(index='month', columns='year', values='passengers')
print(df_pivot.index)

st.table(df_pivot)

st.line_chart(df_pivot, x_label='Mes', y_label='Pasajeros')

# 3. area_chart
st.header('Gráfico de área: st.area_chart')
#st.area_chart(df_pivot)
fmri_df = sns.load_dataset('fmri')
st.table(fmri_df.head())
# Agrupamos por timepoint y region, y sacamos la media de la señal
fmri_grouped = fmri_df.groupby(['timepoint', 'region'])['signal'].mean().unstack()
st.area_chart(fmri_grouped)


# 4. Mapa
st.header('Gráfico de mapa: st.map')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [19.43, -99.13],
    columns=['lat', 'lon']
)
st.map(map_data)

# 5. Scatter

st.header('Gráfico de scatter: st.scatter_chart')
st.scatter_chart(df_tips, x='total_bill', y='tip', color='sex')