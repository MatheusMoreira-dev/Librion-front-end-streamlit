import streamlit as st
import componentes

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
            st.switch_page("pages/2_Login.py")
    with c2:
        if st.button("Explorar acervo", use_container_width=True):
            st.switch_page("pages/1_Catalogo.py")
    
    # Imagem de destaque (podes trocar pela imagem real do teu projeto)
    st.image("https://images.unsplash.com/photo-1481627581964-f141f00567b7?q=80&w=2000", use_container_width=True)

st.write("##") # Espaçamento
st.divider()

# --- SEÇÃO DE RECURSOS (Os 4 cards inferiores) ---
st.write("##")
f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("### 📖")
    st.markdown("**Acervo Completo**")
    st.caption("Acesse milhares de livros de todas as bibliotecas municipais.")

with f2:
    st.markdown("### 🕸️")
    st.markdown("**Rede Integrada**")
    st.caption("Solicite livros de outras unidades sem sair de casa.")

with f3:
    st.markdown("### 👥")
    st.markdown("**Comunidade Leitora**")
    st.caption("Faça parte de uma comunidade apaixonada por leitura.")

with f4:
    st.markdown("### 🏅")
    st.markdown("**Recomendações**")
    st.caption("Receba sugestões personalizadas de leitura baseadas no seu perfil.")