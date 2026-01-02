import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Librion - Rede de Bibliotecas", layout="wide")

def main():
    # --- 1. CABEÇALHO / NAVBAR ---
    # Criando colunas para distribuir o logo e os links de menu
    col_logo, col_nav, col_login = st.columns([2, 5, 1])

    with col_logo:
        st.markdown("### 📘 Librion")
        st.caption("Rede Municipal de Bibliotecas")

    with col_nav:
        # Criando um menu simples usando colunas internas
        m1, m2, m3, m4 = st.columns(4)
        m1.button("Início", use_container_width=True)
        m2.button("Catálogo", use_container_width=True)
        m3.button("Sobre", use_container_width=True)
        m4.button("Ajuda", use_container_width=True)

    with col_login:
        st.button("Entrar", type="primary")
        
    st.divider() # Linha horizontal para separar

    # --- 2. SEÇÃO HERO (DESTAQUE) ---
    # Como não usamos CSS para sobrepor texto à imagem,
    # usamos uma organização vertical limpa.
    
    st.title("Conectando todas as bibliotecas em um só lugar")
    st.subheader("Acesse o acervo completo da Rede Municipal de Bibliotecas de Crato-CE.")
    st.write("Pegue livros de qualquer unidade com facilidade.")
    
    col_btn1, col_btn2, _ = st.columns([2, 2, 6])
    with col_btn1:
        st.button("Acessar minha conta", use_container_width=True, type="primary")
    with col_btn2:
        st.button("Explorar acervo", use_container_width=True)

    # Espaçamento
    st.write("##")
    st.divider()

    # --- 3. SEÇÃO DE RECURSOS (COLUNAS) ---
    # Criando 4 colunas para os ícones e textos informativos
    feat1, feat2, feat3, feat4 = st.columns(4)

    with feat1:
        st.markdown("### 📖", text_alignment="center")
        st.markdown("**Acervo Completo**", text_alignment="center")
        st.markdown("Acesse milhares de livros de todas as bibliotecas municipais.", text_alignment="center")

    with feat2:
        st.markdown("### 🕸️", text_alignment="center")
        st.markdown("**Rede Integrada**", text_alignment="center")
        st.markdown("Solicite livros de outras unidades sem sair de casa.")

    with feat3:
        st.markdown("### 👥", text_alignment="center")
        st.markdown("**Comunidade Leitora**", text_alignment="center")
        st.markdown("Faça parte de uma comunidade apaixonada por leitura.")

    with feat4:
        st.markdown("### 🏅", text_alignment="center")
        st.markdown("**Recomendações**", text_alignment="center")
        st.markdown("Receba sugestões personalizadas de leitura.", text_alignment="center")

if __name__ == "__main__":
    main()