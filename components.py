import streamlit as st

# Cabeçalho Base
def base_header():
    cols = st.columns(4)

    with cols[0]:
        st.markdown("### 📘 Librion")
        st.caption("Rede Municipal de Bibliotecas")

    if cols[1].button("🏠 Início", use_container_width=True, key="btn_header_home"):
        st.switch_page("home.py")
        
    if cols[2].button("🔍 Catálogo", use_container_width=True, key="btn_header_catalog"):
        st.switch_page("pages/1_catalogo.py")
    
    if cols[3].button("ℹ️ Sobre", use_container_width=True, key="btn_header_about"):
        st.switch_page("pages/3_sobre.py")

# Cabeçalho do visitante
def visitor_header():
    col1, col2, col3 = st.columns([5,2,1])

    with col1:
        base_header()

    with col3:
        if st.button("Login", type="primary", use_container_width=True, key="btn_header_login"):
            st.switch_page("pages/2_login.py")

# Cabeçalho do usuário
def user_header():
    col1, col2, col3, col4 = st.columns([5,1,1,1])

    with col1:
        base_header()

    with col3:
        if st.button("👤 Minha Conta", type="primary", width='stretch'):
            st.switch_page("pages/7_minha_conta.py")

    with col4:
        if st.button("Sair", type="tertiary", width="stretch"):
            pass

# Cabeçalho de admin
def admin_header():
    cols = st.columns(7)

    with cols[0]:
        st.markdown("### 📘 Librion")
        st.caption("Rede Municipal de Bibliotecas")

    with cols[1]:
        if st.button("📝 Exemplares", use_container_width=True):
            st.switch_page("pages/4_admin_livros.py")
        
    with cols[2]:
        if st.button("👥 Usuários", use_container_width=True):
            st.switch_page("pages/5_admin_usuarios.py")
    
    with cols[3]:
        if st.button("🏢 Bibliotecas", use_container_width=True):
            st.switch_page("pages/6_admin_bibliotecas.py")
    
    with cols[5]:
        if st.button("👤 Minha Conta", type="primary", use_container_width=True):
            st.switch_page("pages/7_minha_conta.py")

    with cols[6]:
        if st.button("Sair", type="tertiary", width="stretch"):
            pass

# Renderiza o cabeçalho
def render_header():
    user = st.session_state.get("user")
    
    if not user:
        visitor_header()
    
    elif user["admin"]:
        admin_header()
    
    else:
        user_header()

def render_cards():
    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.markdown("### 📖", text_alignment="center")
        st.markdown("**Acervo Completo**", text_alignment="center")
        st.caption("Acesse milhares de livros de todas as bibliotecas municipais.", text_alignment="center")

    with f2:
        st.markdown("### 🕸️", text_alignment="center")
        st.markdown("**Rede Integrada**", text_alignment="center")
        st.caption("Solicite livros de outras unidades sem sair de casa.", text_alignment="center")

    with f3:
        st.markdown("### 👥", text_alignment="center")
        st.markdown("**Comunidade Leitora**", text_alignment="center")
        st.caption("Faça parte de uma comunidade apaixonada por leitura.", text_alignment="center")

    with f4:
        st.markdown("### 🏅", text_alignment="center")
        st.markdown("**Recomendações**", text_alignment="center")
        st.caption("Receba sugestões personalizadas de leitura baseadas no seu perfil.", text_alignment="center")