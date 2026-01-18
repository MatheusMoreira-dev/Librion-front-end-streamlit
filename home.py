import streamlit as st
from components import visitor_header, render_header, render_cards

# Configuração da página
st.set_page_config(
    page_title="Librion - Conectando Bibliotecas", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

def render_highlights():
    with st.container(width='stretch'):
        st.markdown("# Conectando todas as bibliotecas em um só lugar")
        st.markdown("##### Acesse o acervo completo da Rede Municipal de Bibliotecas de Crato-CE. Empreste livros de qualquer unidade com facilidade.")

    st.markdown("##")
    render_cards()

def render_page():
    render_header(visitor_header)
    render_highlights()

render_page()