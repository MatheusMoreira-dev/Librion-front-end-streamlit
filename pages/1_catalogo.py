import streamlit as st
import componentes
from utils.api import do_get, do_post

# Configuração da página
st.set_page_config(page_title="Librion | Catálogo", layout="wide")

# Exibir o menu superior (que criámos anteriormente)
componentes.menu_superior()

# Cabeçalho
def header():
    st.title("Catálogo")
    st.write("Explore o acervo completo da Rede Municipal de Bibliotecas de Crato-CE")

# Busca os livros na API
def fetch_books(filters = None):
    if filters:
        return do_post("/books/search", json=filters)
    else:
        return do_get("/books")

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
    all_libraries = do_get("/libraries")

    with st.container(border=True):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.text_input("Título", placeholder="Ex: Viagem ao Centro da Terra", key="title")
        
        with col2:
            st.multiselect("Filtra por biblioteca", options=all_libraries, format_func= lambda l:l["name"], key="libraries")

        with st.container():
            __, center, __ = st.columns([4,2,4])
            
            with center:
                col1, col2 = st.columns(2)
                
                with col1:
                    submit = st.button("Buscar",type='primary',width='stretch', on_click=filter_books)
                
                with col2:
                    clear = st.button("Limpar Filtros", type='secondary', width='stretch', on_click=clear_filters)

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

    if total_books > 0:
        st.subheader(f"Resultado: {total_books} livro(s) encontrados")

    else:
        st.subheader("Nenhum livro encontrado!")

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
    render_filters()
    render_grid(st.session_state.books)

render_page()