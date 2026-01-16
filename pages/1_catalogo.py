import streamlit as st
import componentes
from utils.api import do_get

# Configuração da página
st.set_page_config(page_title="Librion - Catálogo", layout="wide")

# Exibir o menu superior (que criámos anteriormente)
componentes.menu_superior()

def cabecalho():
    st.title("Catálogo")
    st.write("Explore o acervo completo da Rede Municipal de Bibliotecas de Crato-CE")

def filtros():
    col_busca, col_genero, col_biblio = st.columns([2, 1, 1])

    with col_busca:
        termo = st.text_input("🔍 Buscar por título ou autor...", placeholder="Ex: Machado de Assis")

    with col_genero:
        genero = st.selectbox("Filtro: Género", ["Todos os géneros", "Romance", "Clássico", "Drama"])

    with col_biblio:
        biblioteca = st.selectbox("Filtro: Unidade", ["Todas as bibliotecas", "Centro", "Pinto Madeira", "Seminário"])

    st.write(f"**{12} livros encontrados**") # Exemplo estático, pode ser dinâmico com len()
    st.write("---")

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
             if st.button("Reservar", key=key):
                 st.toast(f"Solicitação enviada: {book['titulo']}")

def grid(books, cols_per_row = 4):
    total_books = len(books)

    for i in range(0, total_books, cols_per_row):
        cols = st.columns(cols_per_row)

        for j in range(min(cols_per_row, total_books - i)):
            with cols[j]:
                card_book(books[i + j], key=i+j)

def main():
    cabecalho()

    filtros()
    
    books = do_get("/books")["books"]
    grid(books)

main()