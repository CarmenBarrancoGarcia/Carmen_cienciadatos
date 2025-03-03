import streamlit as st 
import joblib
import seaborn as sns
import pandas as pd 
from sklearn.preprocessing import LabelEncoder

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_clasificacion.joblib')

st.set_page_config(
    page_title='Clasificación', 
    page_icon=':robot_face:'
)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Volver a Inicio'):
        st.switch_page('app.py')
        
with col2:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 📊 EDAs.py')
        
with col3:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🤖 Regresión.py')
        
        
st.title('Clasificación en dataset Diamonds')

model = load_scikit_model()

st.write('Datos Dataset Diamonds')
df = sns.load_dataset('Diamonds')
st.table(df.head())

# 2. Formulario para predicción
st.header('Introduce datos para la predicción')

with st.form("Formulario_diamonds"):
    carat = st.number_input(
                    'Introduce total quilates (carat)', 
                    min_value=0.0, max_value=10.0, 
                    value=df['carat'].mean(), 
                    step=0.01
    )
    
    color = st.selectbox('Introduce color (color)', df['color'].unique().tolist())
    
    clarity = st.selectbox('Introduce claridad (clarity)', df['clarity'].unique().tolist())
    
    depth = st.number_input(
        'Introduce profundidad (depth)', 
        value=df['depth'].mode()[0], 
        step=0.01
    )
    
    table = st.number_input(
        'Introduce table',
        value=df['table'].mode()[0],
        step=0.01
    )
    
    price = st.number_input(
        'Introduce precio total (price)',
        min_value=0, max_value=1000000,
        value=df['price'].mode()[0],
        step=1
    )
    
    x = st.number_input(
        'Introduce x',
        value=df['x'].mode()[0],
        step=0.01
    )
    y = st.number_input(
        'Introduce y',
        value=df['y'].mode()[0],
        step=0.01
    )
    z = st.number_input(
        'Introduce z', 
        value=df['z'].mode()[0],
        step=0.01
    )
    
    boton_enviar = st.form_submit_button("Generar predicción")
    
    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'price': [price], 
            'x': [x], 
            'y': [y], 
            'z': [z]                        
        })
        prediccion = model.predict(X_new)[0] 
      
        proba = model.predict_proba(X_new).max() * 100
        col1, col2 = st.columns(2)
        col1.metric('Corte estimado (predicción)', value=prediccion)
        col2.metric('Corte medio', value=f'{proba:.2f} $')