import streamlit as st

def menu_superior():
    """
    Desenha a barra de navegação superior da plataforma Librion.
    """
    # Criamos 3 colunas principais: Logo, Links de Navegação, Ações (Login/Sair)
    col_logo, col_nav, col_acao = st.columns([2, 5, 1])

    with col_logo:
        # Estilizamos o logo com Markdown simples
        st.markdown("### 📘 Librion")
        st.caption("Rede Municipal de Bibliotecas")

    with col_nav:
        # Criamos sub-colunas para distribuir os itens do menu horizontalmente
        m1, m2, m3, m4 = st.columns(4)
        
        # Usamos switch_page para navegar entre os ficheiros
        if m1.button("🏠 Início", use_container_width=True):
            st.switch_page("Home.py")
        
        if m2.button("🔍 Catálogo", use_container_width=True):
            st.switch_page("pages/1_Catalogo.py")
            
        if m3.button("ℹ️ Sobre", use_container_width=True):
            # Se ainda não tiveres a página, podes deixar um aviso ou switch_page
            st.switch_page("pages/3_Sobre.py")
            
        if m4.button("❓ Ajuda", use_container_width=True):
            st.toast("Página de 'Ajuda' em desenvolvimento!")

    with col_acao:
        # Lógica de botão dinâmico: se estiver logado mostra 'Sair', senão 'Entrar'
        if st.session_state.get("logado", False):
            if st.button("Sair", type="secondary", use_container_width=True):
                st.session_state.clear() # Limpa a memória (Logout)
                st.rerun()
        else:
            if st.button("Entrar", type="primary", use_container_width=True):
                st.switch_page("pages/2_Login.py")

    st.divider() # Linha que separa o menu do conteúdo da página