import streamlit as st
from components import user_header
from datetime import datetime
from utils import librion_api

# 1. Configuração da página
st.set_page_config(page_title="Librion - Minha Conta", layout="wide")

# Busca os empréstimos na API
def get_loans():
    response = librion_api("", "")
    pass

# Verifica se o usuário está logado
def check_login(user):
    if not user:
        st.error("Por favor, faça login para acessar esta página.")
        st.button("Ir para Login", on_click=lambda: st.switch_page("pages/2_Login.py"))
        st.stop()

# Renderiza o perfil
def render_profile(name, library):
    col_av, col_info = st.columns([1, 8])
    with col_av:
        st.markdown(
            f"<div style='background-color:#456e7d; color:white; border-radius:50%; width:80px; height:80px; display:flex; align-items:center; justify-content:center; font-size:30px;'>{name[0:2]}</div>", unsafe_allow_html=True)

    with col_info:
        st.subheader(st.session_state.user.get("name", "Usuário"))
        st.caption(f"📍 Biblioteca de Referência: {library}")

    st.write("##")

# Renderiza os cartões de métricas
def render_metrics_cards(total_loans, total_books, next_return_date):
    # --- CARDS DE MÉTRICAS ---
    m1, m2, m3 = st.columns(3)
    with m1:
        with st.container(border=True):
            st.write("📖 **Empréstimos Ativos**")
            st.title("2")
            st.progress(2/5, text="2 de 5 permitidos")

    with m2:
        with st.container(border=True):
            st.write("⭐ **Livros Lidos**")
            st.title("28")
            st.caption("neste ano")

    with m3:
        with st.container(border=True):
            st.write("⏰ **Prazo Próximo**")
            st.title("5")
            st.caption("dias para devolução")

    st.write("##")

# Renderiza um empréstimo
def render_book_loan(loan):
    with st.container(border=True):
        book = loan["copy"]
        c1, c2 = st.columns([3, 1])

        with c1:
            st.markdown(f"**{book["name"]}**")
            st.caption(f"{book["author"]}")
            st.write(f"📅 Empréstimo: {loan["request_date"]} | Devolução: {loan["return_date"]}")
        with c2:
            st.info(f"{loan["status"]}")

# Renderiza todos os empréstimos
def render_loans(loans):
    st.markdown("### Histórico de Empréstimos")

    for loan in loans:
        render_book_loan(loan)

def render_page():
    loans = [
        {   
            "copy": {
                "name": "Machado de Assis",
                "author": "algo"
            },
            "request_date": datetime.now(),
            "return_date": datetime.now(),
            "status": "ativo"
        }
    ]


    user_header()
    render_profile("Matheus", "Chique")
    render_loans(loans)

render_page()