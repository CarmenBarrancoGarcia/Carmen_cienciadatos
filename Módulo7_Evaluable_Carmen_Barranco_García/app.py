import streamlit as st 
import seaborn as sns 


st.set_page_config(
    page_title='Home', 
    page_icon=':house:'
)

st.title('Ejercicio Módulo 7: Streamlit con Dataset Diamonds')
st.write('El datset Diamonds contiene información de precio, características de corte, color, quilates, etc.. de casi 54.000 diamantes. Vamos a analizarlo.')

@st.cache_data
def load_tips_data():
    return sns.load_dataset('diamonds')


st.header('1. DataFrame Diamonds')
df = load_tips_data()
st.dataframe(df, use_container_width=True)

st.title('Elige una opción')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 📊 EDAs.py')
        
with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🤖 Regresión.py')
        
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 🤖 Clasificación.py')