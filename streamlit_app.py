import streamlit as st
import google.generativeai as genai

# 1. TUS DATOS (API KEY DIRECTA)
MI_API_KEY = "AIzaSyCda_36NM1gzZ3iXRqC36f4FTuDROmfBM0"

# 2. CONFIGURACIÓN SIMPLE DE LA PÁGINA
st.set_page_config(page_title="Asistente IA", layout="centered")
st.title("🤖 Chat con Gemini")

# 3. PEGA TUS INSTRUCCIONES AQUÍ
MIS_INSTRUCCIONES = """
Eres un asistente experto y servicial. 
Ayuda a mis clientes de forma amable.
"""

# 4. INICIO DE LA IA
try:
    genai.configure(api_key=MI_API_KEY)
    
    # Probamos con el nombre más básico posible
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Escribe tu consulta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Metemos las instrucciones directo en el mensaje para evitar el error 404
            mensaje_completo = f"{MIS_INSTRUCCIONES}\n\nPregunta del cliente: {prompt}"
            response = model.generate_content(mensaje_completo)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Error técnico: {e}")
    st.info("Si el error persiste, intenta generar una NUEVA API Key en Google AI Studio.")
