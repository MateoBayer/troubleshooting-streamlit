import streamlit as st
from utils.data import LINES, PACKAGING_TYPES, CHATBOTS

st.set_page_config(
    page_title="Empaque - MGA Asistentes",
    page_icon="📦",
    layout="wide"
)

def main():
    st.title("📦 Selección de Tipo de Empaque")
    st.markdown("---")
    
    # Verificar si hay una línea seleccionada
    if 'selected_line' not in st.session_state or not st.session_state.selected_line:
        st.error("⚠️ Primero debes seleccionar una línea de producción")
        st.markdown("👈 Ve a la página **🏭 Líneas** para seleccionar una línea")
        return
    
    # Obtener nombre de la línea seleccionada
    selected_line_name = next(
        line['name'] for line in LINES 
        if line['id'] == st.session_state.selected_line
    )
    
    st.markdown(f"### Línea seleccionada: **{selected_line_name}**")
    st.markdown("### Selecciona el tipo de empaque:")
    
    # Mostrar opciones de empaque
    cols = st.columns(2)
    
    for i, packaging in enumerate(PACKAGING_TYPES):
        with cols[i]:
            with st.container():
                st.markdown(f"#### {packaging['name']}")
                
                # Verificar si hay bots disponibles para esta combinación
                bots_available = (
                    st.session_state.selected_line in CHATBOTS and 
                    packaging['id'] in CHATBOTS[st.session_state.selected_line]
                )
                
                if bots_available:
                    bot_count = len(CHATBOTS[st.session_state.selected_line][packaging['id']])
                    st.markdown(f"🤖 **{bot_count}** asistentes disponibles")
                else:
                    st.markdown("🚫 No hay asistentes disponibles")
                
                if st.button(
                    f"Seleccionar {packaging['name']}", 
                    key=f"packaging_{packaging['id']}",
                    use_container_width=True,
                    disabled=not bots_available,
                    type="primary" if st.session_state.get('selected_packaging') == packaging['id'] else "secondary"
                ):
                    st.session_state.selected_packaging = packaging['id']
                    st.session_state.selected_bot = None
                    st.session_state.chat_messages = []
                    st.success(f"✅ {packaging['name']} seleccionado")
                    st.rerun()
                
                st.markdown("---")
    
    # Mostrar bots disponibles si se ha seleccionado un tipo de empaque
    if st.session_state.get('selected_packaging'):
        packaging_name = next(
            pkg['name'] for pkg in PACKAGING_TYPES 
            if pkg['id'] == st.session_state.selected_packaging
        )
        
        st.markdown(f"### 🤖 Asistentes disponibles para {packaging_name}")
        
        if (st.session_state.selected_line in CHATBOTS and 
            st.session_state.selected_packaging in CHATBOTS[st.session_state.selected_line]):
            
            available_bots = CHATBOTS[st.session_state.selected_line][st.session_state.selected_packaging]
            
            cols = st.columns(2)
            for i, bot in enumerate(available_bots):
                with cols[i % 2]:
                    if st.button(
                        f"🤖 {bot['name']}", 
                        key=f"bot_{bot['id']}",
                        use_container_width=True,
                        type="primary"
                    ):
                        st.session_state.selected_bot = bot
                        st.session_state.chat_messages = []
                        st.success(f"✅ Asistente {bot['name']} seleccionado")
                        st.markdown("👉 Ve a la página **🤖 Chat** para comenzar la conversación")
        else:
            st.warning("No hay asistentes disponibles para esta combinación")

if __name__ == "__main__":
    main()