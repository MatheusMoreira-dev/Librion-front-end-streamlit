import streamlit as st
import componentes
import cards

# 1. Configuração da página
st.set_page_config(
    page_title="Librion - Conectando Bibliotecas", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Chamar o menu superior
componentes.menu_superior()

# --- SEÇÃO HERO (Destaque) ---
# Usamos colunas para criar um respiro lateral e focar o conteúdo no centro
_, col_hero, _ = st.columns([1, 8, 1])

with col_hero:
    # Título e Subtítulo impactantes
    st.markdown("# Conectando todas as bibliotecas em um só lugar")
    st.markdown("### Acesse o acervo completo da Rede Municipal de Bibliotecas de Crato-CE. Empreste livros de qualquer unidade com facilidade.")
    
    # Botões de Ação
    c1, c2, _ = st.columns([1.5, 1.5, 7])
    with c1:
        if st.button("Acessar minha conta", type="primary", use_container_width=True):
            st.switch_page("pages/2_login.py")
    with c2:
        if st.button("Explorar acervo", use_container_width=True):
            st.switch_page("pages/1_catalogo.py")
    
    # Imagem de destaque (podes trocar pela imagem real do teu projeto)
    st.image("https://images.unsplash.com/photo-1481627581964-f141f00567b7?q=80&w=2000", use_container_width=True)

st.write("##") # Espaçamento
st.divider()

# --- SEÇÃO DE RECURSOS (Os 4 cards inferiores) ---
st.write("##")
cards.exibir_cards()