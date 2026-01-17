import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Mi Asistente IA", layout="wide")

# Barra lateral igual a AI Studio
with st.sidebar:
    st.title("⚙️ Configuración")
    api_key = st.text_input("Pega tu API Key de Google", type="password")
    st.info("Obtén tu llave en aistudio.google.com")
    
    st.divider()
    model_choice = st.selectbox("Modelo", ["gemini-1.5-flash", "gemini-1.5-pro"])
    temp = st.slider("Temperatura (Creatividad)", 0.0, 2.0, 1.0)

st.title("💬 Mi Chat Profesional")

if not api_key:
    st.warning("Por favor, introduce tu API Key en la barra lateral para comenzar.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_choice)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar el chat
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("¿En qué puedo ayudarte?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Respuesta de la IA
        response = model.generate_content(prompt, generation_config={"temperature": temp})
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.chat_message("assistant").write(response.text)
