import streamlit as st
import pandas as pd
from components import render_header
from utils.api import librion_api

# Configuração da página
st.set_page_config(page_title="Librion | Catálogo", layout="wide")

# Busca os livros na API
def fetch_books(filters = None):
    if filters:
        response = librion_api("POST", "/books/search", json=filters)

    else:
        response = librion_api("GET", "/books")

    if response["success"]:
        return response["data"]
    
    st.error("Erro na requisição dos livros")
    st.stop()       
        
# Busca na session os filtros selecionados
def filter_books():
    filters = {
        "title" : st.session_state.title if not "" else None,
        "library_ids": list(map(lambda l:int(l["id"]), st.session_state.libraries))
    }

    # Busca na API os livros filtrados e salva em uma "variável" de estado "books"
    st.session_state.books = fetch_books(filters)

# Limpa os filtros a atualiza o grid
def clear_filters():
    st.session_state.title = None
    st.session_state.libraries = []

    st.session_state.books = fetch_books()

# Formulário para filtragem
def render_filters():
    # bibliotecas da API
    response = librion_api("GET", "/libraries")

    if response["success"]:
        all_libraries = response["data"]

        with st.container(border=True):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.text_input("Título", placeholder="Ex: Viagem ao Centro da Terra", key="title")
            
            with col2:
                st.multiselect("Filtra por biblioteca",placeholder="Selecionar" , options=all_libraries, format_func= lambda l:l["name"], key="libraries")

            with st.container():
                __, center, __ = st.columns([4,2,4])
                
                with center:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        submit = st.button("Buscar",type='primary',width='stretch', on_click=filter_books)
                    
                    with col2:
                        clear = st.button("Limpar Filtros", type='secondary', width='stretch', on_click=clear_filters)
    else:
        st.error("Erro na requisição das bibliotecas")
        st.stop()

# Modal com detalhes de um livro
@st.dialog("Detalhes", width='small')
def modal_details(book:dict):
    image = book.get("image")

    __, center, __ = st.columns([1,2,1])

    with center:
        if image and image != "(vazio)":
            st.image(book.get("image"), width='stretch')

    st.header(book.get("title"))
    st.text(book.get("author"))
    st.text(book.get("description"))

# Modal com o nome de todas as bibliotecas que tem o livro disponível
@st.dialog("Empréstimo", width="medium")
def modal_loan(book:dict):
    response = librion_api("GET", f"/books/{book["id"]}/copies")

    if response["success"]:
        copies = response["data"]

        for i in range(len(copies)):
            col1, col2, col3 = st.columns([3,2,1])
            
            copy = copies[i]
            is_available = copy["quantity_available"] > 0
            with col1:
                st.subheader(copy["library"]["name"], text_alignment="left")
        
            with col2:
                if is_available:
                    st.success("Disponível", width='stretch')
                else:
                    st.error("Indisponível", width='stretch')
            
            with col3:
                if is_available:
                    st.button("Solicitar", key=(copy["id_book"]) * i, width='stretch', type='primary')
    else:
        st.error("Errro na requisição das cópias")
        st.stop()

# Layout de um livro
def card_book(book:dict):
    with st.container(border=True, height="stretch"):
        url_image = book.get("image")

        if url_image and not url_image == "(vazio)":
            st.image(url_image, width='stretch')
    
        st.text(book["title"])
        st.caption(f"{book['author']}")
        
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            user = st.session_state.get("user")
            disable_button = True if not user or user["admin"] else False

            btn_loan = st.button("Empréstimo", type="primary", width='stretch', key=f"loan_{book["id"]}", disabled=disable_button)

            if btn_loan:
                modal_loan(book)
        
        with btn_col2:
             btn_details = st.button("Detalhes", type= "tertiary",  width='stretch', key=f'detail_{book["id"]}') 
             
             if btn_details:
                 modal_details(book)

# Renderiza um grid com os livros
def render_grid(books, cols_per_row = 5):
    total_books = len(books)

    if total_books > 0:
        st.subheader(f"Resultado: {total_books} livro(s) encontrados")

    else:
        st.subheader("Nenhum livro encontrado!")

    for i in range(0, total_books, cols_per_row):
        cols = st.columns(cols_per_row)

        for j in range(min(cols_per_row, total_books - i)):
            with cols[j]:
                card_book(books[i + j])

# Renderiza a página
def render_page():
    # Criar uma variável de "estado" para a lista de livros    
    if "books" not in st.session_state:
        st.session_state.books = fetch_books()

    render_header()
    
    st.title("Catálogo")
    st.write("Explore o acervo completo da Rede Municipal de Bibliotecas de Crato-CE")
    
    render_filters()
    render_grid(st.session_state.books)

render_page()