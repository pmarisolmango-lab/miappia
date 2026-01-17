import streamlit as st
import google.generativeai as genai

# 1. CONFIGURACIÓN DE LA VENTANA (Lo que ve el cliente)
st.set_page_config(page_title="Asistente Virtual", layout="centered")

st.title("🤖 Mi Asistente Inteligente")
st.write("Bienvenido. Puedes hacerme cualquier consulta abajo.")

# 2. TUS DATOS SECRETOS (Ya están cargados aquí)
MI_API_KEY = "AIzaSyCda_36NM1gzZ3iXRqC36f4FTuDROmfBM0"

# --- PEGA TUS INSTRUCCIONES DE GOOGLE AI STUDIO AQUÍ ABAJO ---
MIS_INSTRUCCIONES = """
Eres un asistente experto y servicial. 
Tu objetivo es ayudar a mis clientes de forma amable y profesional.
"""
# ------------------------------------------------------------

# 3. LÓGICA PARA QUE FUNCIONE (No tocar esto)
try:
    genai.configure(api_key=MI_API_KEY)
    
    # Hemos corregido el nombre del modelo para que no de error "NotFound"
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash", 
        system_instruction=MIS_INSTRUCCIONES
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes anteriores del chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat en tiempo real
    if prompt := st.chat_input("Escribe tu mensaje aquí..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Respondiendo..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Error técnico: {e}")
    st.info("Asegúrate de que tu API Key sea correcta y esté activa.")
