import streamlit as st
import google.generativeai as genai

# 1. CONFIGURACIÓN DE LA VENTANA
st.set_page_config(page_title="Asistente Virtual", layout="centered")

st.title("🤖 Mi Asistente Inteligente")
st.write("Bienvenido. Puedes hacerme cualquier consulta abajo.")

# 2. TUS DATOS (Tu Key ya está aquí)
MI_API_KEY = "AIzaSyCda_36NM1gzZ3iXRqC36f4FTuDROmfBM0"

# --- PEGA TUS INSTRUCCIONES AQUÍ ABAJO ---
MIS_INSTRUCCIONES = """
Eres un asistente experto y servicial. 
Tu objetivo es ayudar a mis clientes de forma amable y profesional.
"""
# ------------------------------------------------------------

# 3. LÓGICA PARA QUE FUNCIONE
try:
    genai.configure(api_key=MI_API_KEY)
    
    # CAMBIO AQUÍ: Usamos 'gemini-pro' que es el más estable para esta conexión
    model = genai.GenerativeModel(
        model_name="gemini-pro"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes anteriores
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
                # Enviamos las instrucciones junto con el mensaje para que no falle
                full_prompt = f"{MIS_INSTRUCCIONES}\n\nUsuario: {prompt}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Error técnico: {e}")
