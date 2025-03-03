import streamlit as st 
import joblib
import seaborn as sns
import pandas as pd 

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_regresion.joblib')

st.set_page_config(
    page_title='Regresión', 
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
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 🤖 Clasificación.py')
        
st.title('Regresión en dataset Diamonds')

model = load_scikit_model()

st.write('Datos Dataset Diamonds')
df = sns.load_dataset('Diamonds')
price_mean = df['price'].mean() 

st.table(df.head())

# 2. Formulario para predicción
st.header('Introduce datos para la predicción')

with st.form("Formulario_diamonds"):
    carat = st.number_input(
                    'Introduce total quilate', 
                    min_value=0.0, max_value=10.0, 
                    value=df['carat'].mean(), 
                    step=0.01
    )
    
    cut = st.selectbox('Introduce corte (cut)', df['cut'].unique().tolist())
    
    color = st.selectbox('Introduce color (color)', df['color'].unique().tolist())
    
    clarity = st.selectbox('Introduce claridad (clarity)', df['clarity'].unique().tolist())
    
    depth = st.number_input(
        'Introduce profundidad', 
        value=df['depth'].mode()[0], 
        step=0.01
    )
    
    table = st.number_input(
    'Introduce table',
    value=df['table'].mode()[0],
    step=0.01
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
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table], 
            'x': [x], 
            'y': [y], 
            'z': [z]                        
        })
        prediccion = model.predict(X_new)[0] 
      
        delta_value = prediccion - price_mean
        col1, col2 = st.columns(2)
        col1.metric('Precio estimada (predicción)', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
        col2.metric('Precio medio', value=f'{price_mean:.2f} $')
