import streamlit as st
import componentes

# 1. Configuração da página
st.set_page_config(page_title="Sobre o Librion", layout="wide")

# 2. Menu Superior
componentes.menu_superior()

# --- BANNER DE BOAS-VINDAS ---
# Usamos um container com borda para destacar a mensagem principal
with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>Bem-vindo ao Librion</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>O sistema integrado de gerenciamento das bibliotecas municipais de Crato, Ceará</p>", unsafe_allow_html=True)

st.write("##")

# --- TEXTO INSTITUCIONAL ---
with st.container(border=True):
    st.subheader("Sobre o Librion")
    st.write("""
    O Librion é uma plataforma inovadora que conecta todas as bibliotecas municipais de Crato-CE em uma única rede integrada. 
    Nosso objetivo é democratizar o acesso ao conhecimento, facilitando o empréstimo de livros e a gestão do acervo bibliográfico.
    
    Com o Librion, você pode acessar o catálogo completo de todas as bibliotecas municipais, fazer reservas online e solicitar livros 
    de outras unidades, tudo isso de forma simples e intuitiva.
    
    O nome "Librion" combina "Library" (biblioteca) com "Lion" (leão), simbolizando força, conhecimento e a união de todas as 
    bibliotecas em uma grande rede de sabedoria.
    """)

st.write("##")

# --- GRID DE RECURSOS (2x2) ---
col_rec1, col_rec2 = st.columns(2)

with col_rec1:
    with st.container(border=True):
        st.markdown("### 📖")
        st.markdown("**Acervo Completo**")
        st.write("Acesse milhares de livros de todas as bibliotecas municipais em um único lugar.")

    with st.container(border=True):
        st.markdown("### 👥")
        st.markdown("**Comunidade**")
        st.write("Faça parte de uma comunidade apaixonada por leitura e conhecimento.")

with col_rec2:
    with st.container(border=True):
        st.markdown("### 🕸️")
        st.markdown("**Rede Integrada**")
        st.write("Solicite livros de outras unidades e receba na sua biblioteca de referência.")

    with st.container(border=True):
        st.markdown("### 🎗️")
        st.markdown("**Recomendações**")
        st.write("Receba sugestões personalizadas baseadas em suas preferências de leitura.")

st.write("##")

# --- SEÇÃO DE ESTATÍSTICAS (MÉTRICAS) ---
# Usamos uma cor de fundo ou container para destacar os números
st.divider()
st.markdown("<h3 style='text-align: center;'>Nosso Impacto em Números</h3>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(label="Bibliotecas", value="6")
with m2:
    st.metric(label="Livros", value="12,543")
with m3:
    st.metric(label="Usuários", value="8,921")
with m4:
    st.metric(label="Empréstimos Ativos", value="3,247")