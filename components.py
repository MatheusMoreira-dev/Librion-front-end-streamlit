import streamlit as st

def base_header():
    cols = st.columns(3)

    if cols[0].button("🏠 Início", use_container_width=True, key="btn_header_home"):
        st.switch_page("home.py")
        
    if cols[1].button("🔍 Catálogo", use_container_width=True, key="btn_header_catalog"):
        st.switch_page("pages/1_catalogo.py")
    
    if cols[2].button("ℹ️ Sobre", use_container_width=True, key="btn_header_about"):
        st.switch_page("pages/3_sobre.py")

def visitor_header():
    col1, col2, col3 = st.columns([5,2,1])

    with col1:
        base_header()

    with col3:
        if st.button("Login", type="primary", use_container_width=True, key="btn_header_login"):
            st.switch_page("pages/2_login.py")

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

def admin_header():
    cols = st.columns(6)

    with cols[0]:
        if st.button("📝 Exemplares", use_container_width=True):
            st.switch_page("pages/4_admin_livros.py")
        
    with cols[1]:
        if st.button("👥 Usuários", use_container_width=True):
            st.switch_page("pages/5_admin_usuarios.py")
    
    with cols[2]:
        if st.button("🏢 Bibliotecas", use_container_width=True):
            st.switch_page("pages/6_admin_bibliotecas.py")
    
    with cols[4]:
        if st.button("👤 Minha Conta", type="primary", use_container_width=True):
            st.switch_page("pages/7_minha_conta.py")

    with cols[5]:
        if st.button("Sair", type="tertiary", width="stretch"):
            pass

def render_header(header):
    with st.container(width='stretch'):
        col1, col2 = st.columns([1,5])
        
        with col1:
            st.markdown("### 📘 Librion")
            st.caption("Rede Municipal de Bibliotecas")
         
        with col2:
            header()

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

def menu_superior():
    """
    Desenha a barra de navegação superior da plataforma Librion com suporte a perfis.
    """

    render_header()


    st.divider()