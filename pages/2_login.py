import streamlit as st
from components import visitor_header
from utils import librion_api

# Configuração da página para esconder a barra lateral e focar no login
st.set_page_config(page_title="Librion | Login", layout="wide", initial_sidebar_state="collapsed")

def get_acess_token(email, password):
    response = librion_api("POST", "/auth/login", json={"email": email, "password": password})

    if response["success"]:
        st.session_state.acess = response["data"]
        return response["data"]
    
    return None

def get_auth_user(token):
    headers = {}
    headers["Authorization"] =  f"Bearer {token}"

    response = librion_api("")

    pass

def redirect_page(user):
    if user["admin"]:
        st.switch_page("pages/4_admin_livros.py")
    else:
        st.switch_page("pages/7_minha_conta.py")

def card_banner():
    with st.container(border=True): # Simula o card azul da imagem
        st.image("https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1000", caption="Bem-vindo ao Librion")
        st.markdown("### Faça parte da rede integrada de bibliotecas municipais de Crato-CE")

def card_login():
    st.subheader("Acesse sua conta")
    st.write("Entre com suas credenciais para acessar o Librion")
    
    email = st.text_input("E-mail", placeholder="seu@email.com")
    senha = st.text_input("Senha", type="password", placeholder="********")
    
    btn_login = st.button("Fazer Login", type="primary", width='stretch')

    if btn_login:
        if not email.strip() or not senha.strip():
            st.error("Preencha todos os campos!")
            st.stop()

        user = {
            "name": "Matheus",
            "email": "matheus@gmail.com",
            "admin": False
        }

        st.session_state.user = user
        redirect_page(user)
        # token = get_acess_token(email, senha)

        # if token:

def render_page():
    visitor_header()

    _, center, _ = st.columns([1, 4, 1])

    with center:
        col_img, col_form = st.columns([1, 1], gap="large")

        with col_img:
            card_banner()

        with col_form:
            card_login()

render_page()