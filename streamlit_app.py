import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA INTERFAZ ---
st.set_page_config(page_title="Asistente IA Profesional", layout="centered")

# Estilo para que se vea más profesional
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4285f4;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Mi Asistente Gemini")
st.info("Bienvenido a tu asistente inteligente. Escribe tu consulta abajo.")

# --- DATOS DE CONFIGURACIÓN ---
# Tu API Key ya integrada
MI_API_KEY = "AIzaSyCda_36NM1gzZ3iXRqC36f4FTuDROmfBM0" 

# PEGA AQUÍ TUS INSTRUCCIONES DE GOOGLE AI STUDIO
# (Lo que pusiste en 'System Instructions')
MIS_INSTRUCCIONES = """
Eres un asistente experto y servicial. 
Tu objetivo es ayudar a mis clientes de forma amable y profesional.
"""

# --- LÓGICA DE CONEXIÓN ---
try:
    genai.configure(api_key=MI_API_KEY)
    # Usamos Gemini 1.5 Flash que es rápido y económico
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=MIS_INSTRUCCIONES
    )

    # Inicializar el historial de chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes previos
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada de usuario
    if prompt := st.chat_input("¿En qué puedo ayudarte hoy?"):
        # Guardar y mostrar mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar y mostrar respuesta de la IA
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Hubo un error de conexión: {e}")
