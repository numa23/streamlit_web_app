import streamlit as st
from PIL import Image

#pythonProject\numa_app> streamlit run .\main_app.py

st.title('numa23アプリ')
st.caption('これはnuma23の動画用のテストアプリです')

image = Image.open('./data/l_mika2105_shigoto3.jpg')
st.image(image, width=200)
