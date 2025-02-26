import streamlit as st 
import seaborn as sns 

st.title('Ejemplo de formulario Streamlit')

df = sns.load_dataset('tips')
st.header('Ejemplo de botón interactivo')
st.write('Si no se hace clic entonces muestra una tabla con 5 filas, si hace clic muestra todo el dataFrame.')
clicked = st.button('Mostrar dataframe completo', type='primary')
if not clicked:
    st.table(df.head())
else:
    st.dataframe(df, use_container_width=True)

st.header('Formularios')
# Creamos un formulario llamado "mi_fomulario"
with st.form('mi_formulario'):
    st.write('Por favor, complete los siguientes campor:')
    
    # Texto de una línea
    nombre = st.text_input('Nombre', placeholder='Juancito')
     
    # Texto de varias líneas
    descripcion = st.text_area('Descripción', placeholder='Descripción texto largo pero tampoco mucho')
    
    # Número (con límites y paso específico)
    edad = st.number_input('Edad', min_value=0, max_value=120, value=25, step=1)
    
    # Slider (control deslizable)
    peso = st.slider('Peso (kg)', 0, 150, 75) # se puede hacer rango y que permita seleccionar mínimo y máximo
    
    # Selectbox (selección de una opción entre varias)
    genero = st.selectbox('Género', ['Masculino', 'Femenino', 'Otro'])
    
    # Multiselect -- Selección múltiple
    intereses = st.multiselect('Intereses',
                               ['Avistamiento de aves', 'Programación', 'Arte', 'Lectura'])
    
    # Selección de radio
    nivel_experiencia = st.radio("Nivel de experiencia en Python", 
                                 ["Principiante", "Intermedio", "Avanzado"])
    
    # Checkbox (casilla de verificación)
    terminos = st.checkbox('Acepto los términos')
    
    # Hora
    hora = st.time_input('Hora')
    
    # Fecha
    fecha = st.date_input('Fecha')
    
    # Selector de color
    color_favorito = st.color_picker("Elige tu color favorito", "#FFFFFF")
    
    # Subida de archivos
    archivo_subido = st.file_uploader("Sube un archivo", type=["png", "jpg", "pdf"])

    
    # Botón para enviar el formulario
    boton_enviar = st.form_submit_button('Enviar')
    
    # Si el usuario hace clic en el botón "Enviar", mostramos los datos introducidos
    if boton_enviar:
        st.write(f'-**Nombre:** {nombre}')
        st.write(f'-**Descripción:** {descripcion}')
        st.write(f'-**Edad:** {edad}')
        st.write(f'-**Peso:** {peso}')
        st.write(f'-**Género:** {genero}')
    
    # Validamos si hay un archivo subido
    if archivo_subido is not None:
        st.write("Archivo subido con éxito:")
        st.write(f"- Nombre del archivo: {archivo_subido.name}")
    else:
        st.write("No se subió ningún archivo.")  
