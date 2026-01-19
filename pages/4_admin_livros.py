import streamlit as st
from components import admin_header
from utils import librion_api

st.set_page_config(page_title="Admin - Cadastrar Livro", layout="wide")

# Verificação de segurança
def check_login():
    user = st.session_state.get("user")
    is_admin = st.session_state.get("is_admin")

    if not user or not is_admin:
        st.error("Acesso negado! Esta página é restrita a administradores.")
        st.button("Voltar para Home", on_click=lambda: st.switch_page("Home.py"))
        st.stop() # Para a execução aqui

# Registra um novo livro
def register_book(isbn, quantity, is_global = True):
    headers = {"Authorization": f"Beares {st.session_state.token}"}
    body = {"isbn": isbn, "quantity": quantity, "is_global": is_global}
    response = librion_api("POST", "/libraries/me/copies", json=body, headers=headers)

    if response["success"]:
        st.toast("Livro cadastrado com sucesso!")
    
    else:
        st.error(f"Erro no cadastro: {response["error"]}")
        st.stop()

# Cria um novo livro
def render_book_form():
    with st.container(border=True, width='stretch'):
        col1, col2 = st.columns([4,1])
        
        with col1:
            isbn = st.text_input("ISBN")

        with col2:
            quantity = st.number_input("Quantidade de Exemplares", min_value=1, step=1)
            is_global = st.toggle("Global?")

    enviar = st.button("Cadastrar Livro", type="primary")

# Renderiza grade de livros
def render_grid_copies():
    pass

# Renderizar página
def render_page():
    st.title("📑 Gestão de Acervo")
    st.subheader("Cadastrar Novo Livro")

    check_login()
    admin_header()
    render_book_form()

render_page()

# with st.form("form_livro", clear_on_submit=True):
#     col1, col2 = st.columns(2)
    
#     with col1:
#         titulo = st.text_input("Título do Livro")
#         autor = st.text_input("Autor")
#         isbn = st.text_input("ISBN")
    
#     with col2:
#         genero = st.selectbox("Género", ["Romance", "Didático", "Ficção", "Biografia"])
#         unidade = st.selectbox("Biblioteca de Destino", ["Centro", "Pinto Madeira", "Seminário"])
#         quantidade = st.number_input("Quantidade de Exemplares", min_value=1, step=1)

#     resumo = st.text_area("Resumo/Descrição")
    
#     enviar = st.form_submit_button("Cadastrar Livro", type="primary")