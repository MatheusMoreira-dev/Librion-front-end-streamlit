import streamlit as st
from components import admin_header
from utils import librion_api

#configuracao da pagina
st.set_page_config(page_title="Admin - Usuários", layout="wide")

#verificação de login
def check_login():
    user = st.session_state.get("user")
    is_admin = st.session_state.get("is_admin")

    if not user or not is_admin:
        st.error("Acesso negado! Esta página é restrita a administradores.")
        st.button("Voltar para Home", on_click=lambda: st.switch_page("Home.py"))
        st.stop()

#renderiza o formulário do escritor
def render_reader_form():
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
                response = create_reader(nome, email, cep, senha)

                if response["success"]:
                    st.success("Usuário cadastrado com sucesso!")
                    st.balloons()
                else:
                    st.error("Erro ao cadastrar usuário")

# Renderiza os usuário cadastros
def render_list_readers(users):
    st.subheader("Usuários Cadastrados")

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

#POST Reader
def create_reader(name, email, cep, password):
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

def get_readers():
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

def render_page():
    check_login()
    
    admin_header()

    st.title("👥 Gestão de Usuários")
    tab1, tab2 = st.tabs(["🆕 Cadastrar Novo", "📋 Lista de Usuários"])
    
    with tab1:
        render_reader_form()
    
    with tab2:
        render_list_readers("")

render_page()