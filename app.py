import streamlit as st
from PIL import Image

st.title ("Aplicación Inteligencia Urbana")
st.header ("Este es un espacio de aprendizaje sobre ciudades inteligentes")

image = Image.open('imagen.jpg')
st.image(image, caption = 'buenos días')


