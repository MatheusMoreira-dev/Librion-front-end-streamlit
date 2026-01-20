import streamlit as st
from components import admin_header
from utils import librion_api

st.set_page_config(page_title="Admin - Cadastrar Livro", layout="wide")

#verificação de login
def check_login():
    user = st.session_state.get("user")
    is_admin = st.session_state.get("is_admin")

    if not user or not is_admin:
        st.error("Acesso negado! Esta página é restrita a administradores.")
        st.button("Voltar para Home", on_click=lambda: st.switch_page("Home.py"))
        st.stop()

#registra um novo livro
def register_book(isbn, quantity, is_global=True):
    headers = {"Authorization": f"Bearer {st.session_state.token}"}

    body = {
        "isbn": isbn,
        "quantity": quantity,
        "is_global": is_global
    }

    response = librion_api(
        "POST",
        "/libraries/me/copies",
        json=body,
        token=st.session_state.auth_token
    )

    if response["success"]:
        st.toast("Livro cadastrado com sucesso!")
    else:
        st.error(f"Erro no cadastro: {response['error']}")
        st.stop()

#excluir livro
def delete_book(copy_id):
    headers = {"Authorization": f"Bearer {st.session_state.token}"}

    response = librion_api(
        "DELETE",
        f"/libraries/me/copies/{copy_id}",
        token=st.session_state.auth_token
    )

    if response["success"]:
        st.toast("Livro removido com sucesso!")
        st.rerun()
    else:
        st.error(f"Erro ao excluir: {response['error']}")

#formulario cadastro livro
def render_book_form():
    with st.container(border=True, width='stretch'):
        col1, col2 = st.columns([3, 1])

        with col1:
            isbn = st.text_input("ISBN")

        with col2:
            quantity = st.number_input(
                "Quantidade de Exemplares",
                min_value=1,
                step=1
            )

            is_global = st.toggle("Global?")

    if st.button("Cadastrar Livro", type="primary"):
        if not isbn:
            st.warning("Informe o ISBN")
            return

        register_book(isbn, quantity, is_global)

#lista de livros (sem grid)+botao excluir
def render_book_list():
    st.divider()
    st.subheader("📚 Livros Cadastrados")

    #API DESATIVADA (MOCK)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    books = [
        {
            "id": 1,
            "quantity": 3,
            "quantity_available": 2,
            "book": {
                "title": "O Alquimista",
                "author": "Paulo Coelho",
                "isbn": "9788584390670",
                "image": "",
                "description": "Um jovem pastor parte em busca de um tesouro e descobre muito mais sobre si mesmo e seus sonhos."
            }
        },

        {
            "id": 2,
            "quantity": 5,
            "quantity_available": 5,
            "book": {
                "title": "Dom Casmurro",
                "author": "Machado de Assis",
                "isbn": "9788535910667",
                "image": "",
                "description": "Clássico da literatura brasileira que conta a história de Bentinho e Capitu."
            }
        }
    ]
    #renderização

    if not books:
        st.info("Nenhum livro cadastrado ainda.")
        return

    for item in books:
        book = item["book"]

        with st.container(border=True):
            col1, col2, col3 = st.columns([1, 3, 1])

            #imagem do livro
            with col1:
                image = (
                    book["image"]
                    if book["image"]
                    else "https://placehold.co/150x220?text=Sem+Capa"
                )

                st.image(image, width=140)

            #informações do livro
            with col2:
                st.markdown(f"### {book['title']}")
                st.write(f"**Autor:** {book['author']}")
                st.write(f"**ISBN:** {book['isbn']}")

                st.write(
                    f"**Disponíveis:** {item['quantity_available']} "
                    f"de {item['quantity']}"
                )

                with st.expander("Descrição"):
                    st.write(book["description"])

            #botao excluir
            with col3:
                st.write("")  
                st.write("")

                if st.button("🗑 Excluir", key=f"del_{item['id']}"):
                    delete_book(item["id"])


#pag principal
def render_page():
    st.title("📑 Gestão de Acervo")
    st.subheader("Cadastrar Novo Livro")

    check_login()
    admin_header()

    render_book_form()
    render_book_list()


render_page()
