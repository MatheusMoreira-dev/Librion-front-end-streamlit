import streamlit as st
from components import render_header, user_header

# 1. Configuração da página e Menu
st.set_page_config(page_title="Admin - Usuários", layout="wide")
render_header(user_header)

# Verificação de segurança simples (opcional, mas recomendada)
if not st.session_state.get("logado") or st.session_state.get("perfil") != "admin":
    st.error("Acesso restrito a administradores.")
    st.stop()

st.title("👥 Gestão de Usuários")

# Abas para organização
tab1, tab2 = st.tabs(["🆕 Cadastrar Novo", "📋 Lista de Usuários"])

# --- ABA 1: CADASTRO ---
with tab1:
    with st.container(border=True):
        st.subheader("Informações do Novo Usuário")
        
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome Completo", placeholder="Ex: José da Silva")
            email = st.text_input("E-mail de Acesso", placeholder="exemplo@email.com")
        
        with col2:
            tipo = st.radio("Tipo de Perfil", ["Leitor", "Administrador"], horizontal=True)
            st.info("🔑 **Senha Padrão:** `librion123`  \n*O usuário será obrigado a alterá-la no primeiro acesso.*")

        if st.button("Criar Conta", type="primary", use_container_width=True):
            if nome and email:
                # Simulando a lógica de salvar no Banco de Dados
                # No futuro, aqui teremos o POST para o FastAPI enviando:
                # { "nome": nome, "email": email, "perfil": tipo, "senha": "librion123", "trocar_senha": True }
                
                st.success(f"Conta para **{nome}** criada com sucesso!")
                st.balloons()
            else:
                st.warning("⚠️ Por favor, preencha o nome e o e-mail.")

# --- ABA 2: LISTAGEM ---
with tab2:
    st.subheader("Usuários Cadastrados")
    
    # Simulação de dados vindo do SQL (adicionada a coluna de Primeiro Acesso)
    dados_usuarios = [
        {"ID": 1, "Nome": "João Silva", "Perfil": "Leitor", "Status": "Ativo", "Reset Senha": "Não"},
        {"ID": 2, "Nome": "Maria Admin", "Perfil": "Admin", "Status": "Ativo", "Reset Senha": "Não"},
        {"ID": 3, "Nome": "Novo Usuário", "Perfil": "Leitor", "Status": "Pendente", "Reset Senha": "Sim"},
    ]
    
    # Exibe a tabela
    st.dataframe(dados_usuarios, use_container_width=True, hide_index=True)

    st.caption("Nota: 'Reset Senha = Sim' indica que o usuário ainda não alterou a senha padrão.")