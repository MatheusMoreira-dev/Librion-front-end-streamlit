import streamlit as st
from components import visitor_header
from utils import do_get, do_post

# Configuração da página para esconder a barra lateral e focar no login
st.set_page_config(page_title="Librion | Login", layout="wide", initial_sidebar_state="collapsed")

# Exibir o menu superior (que criámos anteriormente)
visitor_header()

def validate_login(email, password):
    validate, error = do_post("/auth/login", json={"email": email, "password": password})

    if error is None and validate.get("access_token") is not None:
        st.session_state.acess = validate
        return validate
    
    return False

def validar_login(email, senha):
    if email == "admin@librion.com" and senha == "123":
        return {"sucesso": True, "perfil": "admin", "nome": "Administrador"}
    elif email == "leitor@email.com" and senha == "123":
        return {"sucesso": True, "perfil": "leitor", "nome": "João Leitor"}
    else:
        return {"sucesso": False, "mensagem": "E-mail ou senha incorretos."}

def card_banner():
    with st.container(border=True): # Simula o card azul da imagem
        st.image("https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1000", caption="Bem-vindo ao Librion")
        st.markdown("### Faça parte da rede integrada de bibliotecas municipais de Crato-CE")

def card_login():
    st.subheader("Acesse sua conta")
    st.write("Entre com suas credenciais para acessar o Librion")
    
    email = st.text_input("E-mail", placeholder="seu@email.com")
    senha = st.text_input("Senha", type="password", placeholder="********")
    
    if st.button("Fazer Login", type="primary", width='stretch'):
        if email == "" or senha == "":
            st.error("Preencha todos os campos!")
            st.stop()
            return

        is_valid = validate_login(email, senha)
        
        if not is_valid:
            st.error("Erro no login. Tente novamente!")
            st.stop()
            return
        
        user, error = do_get("/libraries/me")

        if error != None:
            user = do_get("readers/me")
            st.switch_page("pages/7_minha_conta.py")
            st.session_state.user = user
            return
        
        st.switch_page("pages/4_admin_livros.py")
        st.session_state.user = user

# --- INTERFACE ---
# Criamos margens nas laterais para centralizar o conteúdo [Coluna Vazia, Conteúdo, Coluna Vazia]

def render_page():
    
    _, center, _ = st.columns([1, 4, 1])

    with center:
        col_img, col_form = st.columns([1, 1], gap="large")

        with col_img:
            card_banner()

        with col_form:
            card_login()