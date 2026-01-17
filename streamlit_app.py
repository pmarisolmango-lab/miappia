import streamlit as st
import google.generativeai as genai

# 1. TUS DATOS (API KEY)
MI_API_KEY = "AIzaSyCda_36NM1gzZ3iXRqC36f4FTuDROmfBM0"

# 2. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Asistente IA", layout="centered")
st.title("🤖 Mi Chat Profesional")

# 3. PEGA TUS INSTRUCCIONES AQUÍ
MIS_INSTRUCCIONES = """
Eres un asistente experto y servicial. 
Ayuda a mis clientes de forma amable.
"""

# 4. INICIO DE LA IA
try:
    genai.configure(api_key=MI_API_KEY)
    
    # Nombre técnico exacto para evitar el error 404
    model = genai.GenerativeModel('gemini-1.5-flash')

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
            # Combinamos instrucciones y pregunta en un solo bloque
            prompt_final = f"{MIS_INSTRUCCIONES}\n\nPregunta: {prompt}"
            
            # Usamos una forma de llamado más simple
            response = model.generate_content(prompt_final)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Error técnico: {e}")
    st.info("Si el error persiste, genera una NUEVA API KEY en AI Studio. A veces la primera tarda en activarse.")
