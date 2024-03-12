import streamlit as st
from PIL import Image

st.title ("Aplicación Inteligencia Urbana")
st.header ("Este es un espacio de aprendizaje sobre ciudades inteligentes")

image = Image.open('Imagen.jpg')
st.image(image, caption = 'buenos días')
st.write("Enlace para mi sistema de internet de las cosas")
st.write("Ingresa al [link](https://demo.thingsboard.io/dashboards/e2eb9330-e0a1-11ee-bc03-55147b89654f)")
image = Image.open('Panel ejercicio.png')
st.image(image, caption = 'Panel de control')
