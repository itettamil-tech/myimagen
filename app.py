#pip install streamlit
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image  #pillow
from io import BytesIO

myrobo = genai.Client(api_key="AIzaSyC0odnybhFWVNmGpYeDTL0F3VTW4O_mPBk")

col1,col2=st.columns(2)

with col1:
    st.title("Describer your image here...")
    userData = st.text_area(" ")
    if st.button("Visualize"):
        answer = myrobo.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents= userData,
            config=types.GenerateContentConfig(
                response_modalities = ['TEXT','IMAGE']
                )
            )
        for part in answer.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                image.save("MyImage.png")
with col2:
    if st.image("MyImage.png"):
        st.write("Your image...")
    else:
        st.write("Waiting for your response...")
    
    
