import streamlit as st

def header_admin():
    pass

def header_user():
    pass

def menu_superior():
    """
    Desenha a barra de navegação superior da plataforma Librion com suporte a perfis.
    """
    # Ajustamos as proporções das colunas para acomodar o botão dinâmico na direita
    col_logo, col_nav, col_acao = st.columns([2, 5, 1.5])

    with col_logo:
        st.markdown("### 📘 Librion")
        st.caption("Rede Municipal de Bibliotecas")

    with col_nav:
        # Criamos sub-colunas para os itens de navegação principais
        # Se estiver logado como leitor, adicionamos uma 5ª coluna para "Minha Conta"
        is_leitor = st.session_state.get("perfil") == "leitor"
        n_cols = 5 if is_leitor else 4
        menu_cols = st.columns(n_cols)
        
        if menu_cols[0].button("🏠 Início", use_container_width=True):
            st.switch_page("home.py")
        
        if menu_cols[1].button("🔍 Catálogo", use_container_width=True):
            st.switch_page("pages/1_catalogo.py")
            
        # Novo: Botão Minha Conta aparece apenas para Leitores
        if is_leitor:
            if menu_cols[2].button("👤 Minha Conta", type="primary", use_container_width=True):
                st.switch_page("pages/7_minha_conta.py")
            idx_sobre, idx_ajuda = 3, 4
        else:
            idx_sobre, idx_ajuda = 2, 3

        if menu_cols[idx_sobre].button("ℹ️ Sobre", use_container_width=True):
            st.switch_page("pages/3_sobre.py")
            
        if menu_cols[idx_ajuda].button("❓ Ajuda", use_container_width=True):
            st.toast("Página de 'Ajuda' em desenvolvimento!")

    with col_acao:
        # Lógica de Login/Sair
        if st.session_state.get("logado", False):
            if st.button("Sair", type="secondary", use_container_width=True):
                st.session_state.clear() 
                st.rerun()
        else:
            if st.button("Entrar", type="primary", use_container_width=True):
                st.switch_page("pages/2_login.py")

    # --- MENU DE ADMINISTRADOR ---
    # Só aparece se o perfil for 'admin'
    if st.session_state.get("perfil") == "admin":
        st.write("---") 
        st.caption("🛠️ PAINEL DE ADMINISTRAÇÃO")
        admin_col1, admin_col2, admin_col3, _ = st.columns([1.5, 1.5, 1.5, 5])
        
        with admin_col1:
            if st.button("📝 Gerir Livros", use_container_width=True):
                st.switch_page("pages/4_admin_livros.py")
        with admin_col2:
            if st.button("👥 Gerir Usuários", use_container_width=True):
                st.switch_page("pages/5_admin_usuarios.py")
        with admin_col3:
            if st.button("🏢 Bibliotecas", use_container_width=True):
                st.switch_page("pages/6_admin_bibliotecas.py")

    st.divider()