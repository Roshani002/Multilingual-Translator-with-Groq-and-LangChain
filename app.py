import streamlit as st
from first_llm_translator_app import translate

st.set_page_config(
    page_title="Translator.AI",
    page_icon="🌐",
    layout="centered"
)

# streamit page title
st.title("🌐 Translator App - Groq")

col1, col2 = st.columns(2)

with col1:
    input_languages_list = ["English", "French", "German", "Latin", "Spanish", "Hindi", "Tamil", "Telugu", "Marathi", "Gujarati"]
    input_language = st.selectbox(label="Input Language", options=input_languages_list)
    # input_language = st.selectbox(label="Input Language", options=['English'], index=0)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_languages_list)
    # output_language = st.selectbox(label="Output Language", options=['Italian'], index=0)

input_text = st.text_area("Type the text to be translated")

if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)
    st.success(translated_text)