import streamlit as st
from utils.data import LINES

st.set_page_config(
    page_title="Líneas - MGA Asistentes",
    page_icon="🏭",
    layout="wide"
)

def main():
    st.title("🏭 Selección de Líneas de Producción")
    st.markdown("---")
    
    # Inicializar session state si no existe
    if 'selected_line' not in st.session_state:
        st.session_state.selected_line = None
    
    st.markdown("### Selecciona una línea de producción:")
    
    # Crear grid de botones para las líneas
    cols = st.columns(2)
    
    for i, line in enumerate(LINES):
        with cols[i % 2]:
            # Crear un contenedor con estilo para cada línea
            with st.container():
                st.markdown(f"#### {line['name']}")
                
                if st.button(
                    f"Seleccionar {line['name']}", 
                    key=f"select_{line['id']}",
                    use_container_width=True,
                    type="primary" if st.session_state.selected_line == line['id'] else "secondary"
                ):
                    st.session_state.selected_line = line['id']
                    st.session_state.selected_packaging = None
                    st.session_state.selected_bot = None
                    st.session_state.chat_messages = []
                    st.success(f"✅ Línea {line['name']} seleccionada")
                    st.rerun()
                
                st.markdown("---")
    
    # Mostrar línea actual seleccionada
    if st.session_state.selected_line:
        selected_line_name = next(
            line['name'] for line in LINES 
            if line['id'] == st.session_state.selected_line
        )
        
        st.markdown("### 🎯 Línea Actual")
        st.info(f"**{selected_line_name}** está seleccionada")
        st.markdown("👉 Continúa a la página **📦 Empaque** para seleccionar el tipo de empaque")
    else:
        st.warning("⚠️ No has seleccionado ninguna línea aún")

if __name__ == "__main__":
    main()