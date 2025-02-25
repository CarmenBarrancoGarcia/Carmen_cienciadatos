import streamlit as st 

st.title('Ejemplo de formulario Streamlit')

with st.form('mi_formulario'):
    st.write('Por favor, complete los siguientes campor:')
    
    # Texto de una línea
    nombre = st.text_input('Nombre')
    
    # Texto de varias líneas
    descripcion = st.text_area('Descripción')
    
    # Número
    edad = st.number_input('Edad', min_value=0, max_value=120, value=25, step=1)
    
    # Slider
    peso = st.slider('Peso (kg)', 0, 150, 75)
    
    # Selectbox
    genero = st.selectbox('Género', ['Masculino', 'Femenino', 'Otro'])
    
    # Multiselect -- Selección múltiple
    intereses = st.multiselect('Intereses',['Avistamiento de aves', 'Programación', 'Arte', 'Lectura'])
    
    # Checkbox
    terminos = st.checkbox('Acepto los términos')
    
    # Hora
    hora = st.time_input('Hora')
    
    # Fecha
    fecha = st.date_input('Fecha')
    
    boton_enviar = st.form_submit_button('Enviar')
    
    if boton_enviar:
        st.write(f'-**Nombre:** {nombre}')
        st.write(f'-**Descripción:** {descripcion}')
        st.write(f'-**Edad:** {edad}')
        st.write(f'-**Peso:** {peso}')
        st.write(f'-**Género:** {genero}')
        
