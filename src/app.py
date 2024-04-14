import streamlit as st
from dotenv import load_dotenv
import os
import openai
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Generador de Imágenes de Valen")


# Inicia el formulario
with st.form("images_form"):
    # Agrega un campo de entrada para el texto
    text = st.text_input("Texto para generar imagen")
    
    # Agrega un campo para seleccionar el número de imágenes a generar
    num_images = st.number_input("Número de imágenes a generar", min_value=1, max_value=10, value=1)
    
    # Agrega un campo para seleccionar el tamaño de la imagen
    image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=1)
    
    # Agrega el botón de envío del formulario
    submit_button = st.form_submit_button(label="Generar Imágenes")

# Procesa el formulario cuando se envíe
if submit_button:
    # Aquí puedes realizar cualquier acción que desees cuando se envíe el formulario
  st.write("Generando Imagenes...")

  response = openai.Image.create(
    prompt=text,
    n=num_images,
    size= image_size
    )

for i in range(num_images):
   url = response.data[i].url
   st.image(url,caption=f"Imagenn {i+1}", use_column_width=True)