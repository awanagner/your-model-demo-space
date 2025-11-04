import streamlit as st
from transformers import pipeline

st.title("🚀 My Cool Language Model Demo")

pipe = pipeline("text-generation", model="your-username/your-model")

prompt = st.text_area("Enter your prompt", "Once upon a time")
###
if st.button("Generate"):
    output = pipe(prompt, max_new_tokens=100)
    st.write(output[0]["generated_text"])
