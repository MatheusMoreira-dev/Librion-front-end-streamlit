import streamlit as st
import components
from components import render_cards, render_header

# 1. Configuração da página
st.set_page_config(page_title="Sobre o Librion", layout="wide")

# 2. Menu Superior
render_header()

# --- BANNER DE BOAS-VINDAS ---
# Usamos um container com borda para destacar a mensagem principal
with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>Bem-vindo ao Librion</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>O sistema integrado de gerenciamento das bibliotecas municipais de Crato, Ceará</p>", unsafe_allow_html=True)

st.write("")

# --- TEXTO INSTITUCIONAL ---
with st.container(border=True):
    st.subheader("Sobre o Librion", text_alignment="center")
    st.markdown("""
    O Librion é uma plataforma inovadora que conecta todas as bibliotecas municipais de Crato-CE em uma única rede integrada. 
    Nosso objetivo é democratizar o acesso ao conhecimento, facilitando o empréstimo de livros e a gestão do acervo bibliográfico.
    Com o Librion, você pode acessar o catálogo completo de todas as bibliotecas municipais, fazer reservas online e solicitar livros 
    de outras unidades, tudo isso de forma simples e intuitiva. O nome "Librion" combina "Library" (biblioteca) com "On" (online), simbolizando conhecimento e a união de todas as 
    bibliotecas em uma grande rede de sabedoria.
    """, text_alignment="justify")

st.write("##")

# --- GRID DE RECURSOS (2x2) ---
render_cards()

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