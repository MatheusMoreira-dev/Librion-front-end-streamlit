import streamlit as st
import componentes

# Verificação de segurança
if not st.session_state.get("logado") or st.session_state.get("perfil") != "admin":
    st.error("Acesso negado! Esta página é restrita a administradores.")
    st.button("Voltar para Home", on_click=lambda: st.switch_page("Home.py"))
    st.stop() # Para a execução aqui


st.set_page_config(page_title="Admin - Cadastrar Livro", layout="wide")
componentes.menu_superior()

st.title("📑 Gestão de Acervo")
st.subheader("Cadastrar Novo Livro")

with st.form("form_livro", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        titulo = st.text_input("Título do Livro")
        autor = st.text_input("Autor")
        isbn = st.text_input("ISBN")
    
    with col2:
        genero = st.selectbox("Género", ["Romance", "Didático", "Ficção", "Biografia"])
        unidade = st.selectbox("Biblioteca de Destino", ["Centro", "Pinto Madeira", "Seminário"])
        quantidade = st.number_input("Quantidade de Exemplares", min_value=1, step=1)

    resumo = st.text_area("Resumo/Descrição")
    
    enviar = st.form_submit_button("Cadastrar Livro", type="primary")

if enviar:
    if titulo and autor:
        # Aqui será a integração futura com o FastAPI
        st.success(f"O livro '{titulo}' foi preparado para cadastro no sistema!")
    else:
        st.warning("Por favor, preencha o Título e o Autor.")