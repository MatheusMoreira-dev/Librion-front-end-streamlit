import streamlit as st
import componentes
from utils.api import do_get

# Configuração da página
st.set_page_config(page_title="Librion - Catálogo", layout="wide")

# Exibir o menu superior (que criámos anteriormente)
componentes.menu_superior()

# Cabeçalho
def header():
    st.title("Catálogo")
    st.write("Explore o acervo completo da Rede Municipal de Bibliotecas de Crato-CE")

# Busca os livros na API
def fetch_books(filters = None):
    if filters:
        return do_get("/books/search", params=filters)
    else:
        return do_get("/books")

# Formulário para filtragem
def set_filters():
    # bibliotecas da API
    list_libraries = do_get("/libraries")

    # Formulário de livros
    with st.form("search_form"):
        col1, col2 = st.columns([2, 1])

        with col1:
            title = st.text_input("Título", placeholder="Ex: Viagem ao Centro da Terra")
        
        with col2:
            select_libraries = st.multiselect("Filtra por biblioteca", options=list_libraries, format_func=lambda b:b["name"])

        submit = st.form_submit_button("Buscar")

    # Atualiza a lista de livros em uma "variável" de estado
    if submit:
        filters = {
            "title" : title,
            "library_ids": select_libraries
        }

        st.session_state.books = fetch_books(filters)

# Layout de um livro
def card_book(book:dict, key:int):
    with st.container(border=True, height="stretch"):
        url_image = book.get("image")

        if url_image and not url_image == "(vazio)":
            st.image(url_image, width='stretch')
    
        st.text(book["title"])
        st.caption(f"{book['author']}")
        
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
             if True:
                 st.success("Disponível")
             else:
                 st.warning("Emprestado")
        
        with btn_col2:
             if st.button("Reservar", key=key, width='stretch'):
                 st.toast(f"Solicitação enviada: {book['title']}")

# Renderiza um grid com os livros
def render_grid(books, cols_per_row = 5):
    total_books = len(books)

    for i in range(0, total_books, cols_per_row):
        cols = st.columns(cols_per_row)

        for j in range(min(cols_per_row, total_books - i)):
            with cols[j]:
                card_book(books[i + j], key=i+j)

# Renderiza a página
def render_page():
    # Criar uma variável de "estado" para a lista de livros
    if "books" not in st.session_state:
        st.session_state.books = fetch_books()

    header()
    set_filters()
    
    books = do_get("/books")
    render_grid(books)

render_page()