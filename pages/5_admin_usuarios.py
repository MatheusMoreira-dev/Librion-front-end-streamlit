import streamlit as st
from components import admin_header
# from utils import librion_api   # ← depois você descomenta quando ligar API

#configuracao da pagina
st.set_page_config(page_title="Admin - Usuários", layout="wide")
admin_header()

#verificacao de segurança
#if not st.session_state.get("logado") or st.session_state.get("perfil") != "admin":
#    st.error("Acesso restrito a administradores.")
#    st.stop()

st.title("👥 Gestão de Usuários")

tab1, tab2 = st.tabs(["🆕 Cadastrar Novo", "📋 Lista de Usuários"])

#funcao de cadastro (MOCK)
def create_user(name, email, cep, password):
    """
    Aqui depois vira:
    POST /users
    {
        "name": name,
        "email": email,
        "cep": cep,
        "password": password
    }
    """

    # MOCK simulando sucesso
    return {
        "success": True,
        "data": {
            "name": name,
            "email": email,
            "cep": cep
        }
    }

# funcao de listagem (MOCK)

def get_users():
    """
    Depois vira:
    GET /users
    retorno:
    [
      { "name": "", "email": "", "cep": "" }
    ]
    """

    return [
        {
            "name": "João Silva",
            "email": "joao@email.com",
            "cep": "63010-000"
        },
        {
            "name": "Maria Oliveira",
            "email": "maria@email.com",
            "cep": "58900-000"
        },
        {
            "name": "Carlos Souza",
            "email": "carlos@email.com",
            "cep": "63100-000"
        }
    ]

# ABA 1 – cadastro de usuario
with tab1:
    with st.container(border=True):
        st.subheader("Informações do Novo Usuário")

        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail")

        with col2:
            cep = st.text_input("CEP")
            senha = st.text_input("Senha", type="password")

        if st.button("Criar Conta", type="primary", use_container_width=True):

            if not nome or not email or not cep or not senha:
                st.warning("Preencha todos os campos!")
            else:
                response = create_user(nome, email, cep, senha)

                if response["success"]:
                    st.success("Usuário cadastrado com sucesso!")
                    st.balloons()
                else:
                    st.error("Erro ao cadastrar usuário")

# ABA 2 - lista de usuarios
with tab2:
    st.subheader("Usuários Cadastrados")

    users = get_users()

    #lista visual bonita
    for u in users:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"### {u['name']}")
                st.write(f"📧 **Email:** {u['email']}")
                st.write(f"📍 **CEP:** {u['cep']}")

            with col2:
                st.write("")
                st.write("")
                st.button("🗑 Excluir", key=u["email"])


    # tabela simples
    st.divider()
    st.subheader("Visão em Tabela")

    st.dataframe(
        users,
        use_container_width=True,
        hide_index=True
    )
