import streamlit as st
from utils.data import LINES

# Configuración de la página
st.set_page_config(
    page_title="MGA Asistentes",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🏭 Sistema de Asistentes MGA")
    st.markdown("---")
    
    # Inicializar session state
    if 'selected_line' not in st.session_state:
        st.session_state.selected_line = None
    if 'selected_packaging' not in st.session_state:
        st.session_state.selected_packaging = None
    if 'selected_bot' not in st.session_state:
        st.session_state.selected_bot = None
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    st.markdown("""
    ### Bienvenido al Sistema de Asistentes MGA
    
    Este sistema te permite acceder a diferentes asistentes especializados 
    organizados por líneas de producción y tipos de empaque.
    
    **Instrucciones:**
    1. 🏭 Selecciona una línea de producción
    2. 📦 Elige el tipo de empaque
    3. 🤖 Interactúa con el asistente especializado
    """)
    
    # Mostrar líneas disponibles
    st.markdown("### 🏭 Líneas de Producción Disponibles")
    
    cols = st.columns(3)
    for i, line in enumerate(LINES):
        with cols[i % 3]:
            if st.button(
                line['name'], 
                key=f"line_{line['id']}",
                use_container_width=True,
                type="primary" if st.session_state.selected_line == line['id'] else "secondary"
            ):
                st.session_state.selected_line = line['id']
                st.session_state.selected_packaging = None
                st.session_state.selected_bot = None
                st.session_state.chat_messages = []
                st.rerun()
    
    # Mostrar información de la línea seleccionada
    if st.session_state.selected_line:
        selected_line_name = next(
            line['name'] for line in LINES 
            if line['id'] == st.session_state.selected_line
        )
        st.success(f"✅ Línea seleccionada: **{selected_line_name}**")
        st.info("👉 Dirígete a la página **📦 Empaque** para continuar")

if __name__ == "__main__":
    main()