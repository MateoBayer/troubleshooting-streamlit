import streamlit as st
import asyncio
from utils.data import LINES, PACKAGING_TYPES
from utils.mga_api import mga_client

st.set_page_config(
    page_title="Chat - MGA Asistentes",
    page_icon="🤖",
    layout="wide"
)

def main():
    st.title("🤖 Chat con Asistente MGA")
    st.markdown("---")
    
    # Verificar que se haya seleccionado todo lo necesario
    if (not st.session_state.get('selected_line') or 
        not st.session_state.get('selected_packaging') or 
        not st.session_state.get('selected_bot')):
        
        st.error("⚠️ Configuración incompleta")
        st.markdown("""
        Para usar el chat necesitas:
        1. 🏭 Seleccionar una línea de producción
        2. 📦 Elegir un tipo de empaque  
        3. 🤖 Seleccionar un asistente
        """)
        return
    
    # Obtener información de la selección actual
    line_name = next(line['name'] for line in LINES if line['id'] == st.session_state.selected_line)
    packaging_name = next(pkg['name'] for pkg in PACKAGING_TYPES if pkg['id'] == st.session_state.selected_packaging)
    bot_info = st.session_state.selected_bot
    
    # Mostrar información del contexto actual
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"🏭 **Línea:** {line_name}")
        with col2:
            st.info(f"📦 **Empaque:** {packaging_name}")
        with col3:
            st.info(f"🤖 **Asistente:** {bot_info['name']}")
    
    st.markdown("---")
    
    # Inicializar mensajes del chat si no existen
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    # Mostrar mensajes del chat
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input del chat
    if prompt := st.chat_input("Escribe tu pregunta aquí..."):
        # Agregar mensaje del usuario
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Obtener respuesta del asistente
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    # Preparar mensajes para la API
                    api_messages = []
                    for msg in st.session_state.chat_messages:
                        api_messages.append({
                            "content": msg["content"],
                            "is_user": msg["role"] == "user"
                        })
                    
                    # Llamar a la API de MGA
                    response = asyncio.run(
                        mga_client.ask_question_to_assistant(
                            api_messages, 
                            bot_info['id']
                        )
                    )
                    
                    st.markdown(response)
                    
                    # Agregar respuesta del asistente al historial
                    st.session_state.chat_messages.append({
                        "role": "assistant", 
                        "content": response
                    })
                    
                except Exception as e:
                    error_msg = f"Error al comunicarse con el asistente: {str(e)}"
                    st.error(error_msg)
                    st.session_state.chat_messages.append({
                        "role": "assistant", 
                        "content": error_msg
                    })
    
    # Botones de control
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗑️ Limpiar Chat", use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()
    
    with col2:
        if st.button("🔄 Cambiar Asistente", use_container_width=True):
            st.session_state.selected_bot = None
            st.session_state.chat_messages = []
            st.switch_page("pages/2_📦_Empaque.py")
    
    with col3:
        if st.button("🏠 Inicio", use_container_width=True):
            st.session_state.selected_line = None
            st.session_state.selected_packaging = None
            st.session_state.selected_bot = None
            st.session_state.chat_messages = []
            st.switch_page("main.py")

if __name__ == "__main__":
    main()