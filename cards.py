import streamlit as st

def exibir_cards():
    """
    Função para desenhar cards de recursos na página inicial.
    """
    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.markdown("### 📖", text_alignment="center")
        st.markdown("**Acervo Completo**", text_alignment="center")
        st.caption("Acesse milhares de livros de todas as bibliotecas municipais.", text_alignment="center")

    with f2:
        st.markdown("### 🕸️", text_alignment="center")
        st.markdown("**Rede Integrada**", text_alignment="center")
        st.caption("Solicite livros de outras unidades sem sair de casa.", text_alignment="center")

    with f3:
        st.markdown("### 👥", text_alignment="center")
        st.markdown("**Comunidade Leitora**", text_alignment="center")
        st.caption("Faça parte de uma comunidade apaixonada por leitura.", text_alignment="center")

    with f4:
        st.markdown("### 🏅", text_alignment="center")
        st.markdown("**Recomendações**", text_alignment="center")
        st.caption("Receba sugestões personalizadas de leitura baseadas no seu perfil.", text_alignment="center")