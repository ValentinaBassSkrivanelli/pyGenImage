import streamlit as st
from dotenv import load_dotenv
import os
import openai

# Cargar variables de entorno
load_dotenv()

# Configurar clave de la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Título de la app
st.title("Generador de Imágenes de Valen")

# Formulario de entrada
with st.form("images_form"):
    text = st.text_input("Texto para generar imagen")
    num_images = st.number_input("Número de imágenes a generar", min_value=1, max_value=10, value=1)
    image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=1)
    submit_button = st.form_submit_button(label="Generar Imágenes")

# Procesar formulario
if submit_button:
    if text.strip():  # Verifica que el usuario haya ingresado un texto
        st.write("Generando imágenes...")

        try:
            response = openai.images.generate(
                prompt=text,
                n=num_images,
                size=image_size
            )

            # Mostrar las imágenes generadas
            for i, image_data in enumerate(response.data):
                url = image_data.url
                st.image(url, caption=f"Imagen {i+1}", use_column_width=True)

        except Exception as e:
            st.error(f"Error al generar imágenes: {e}")

    else:
        st.warning("Por favor, ingresa un texto para generar las imágenes.")
