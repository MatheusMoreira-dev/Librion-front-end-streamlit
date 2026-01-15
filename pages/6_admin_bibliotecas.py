import streamlit as st
import componentes

# 1. Configuração da página
st.set_page_config(page_title="Admin - Unidades", layout="wide")
componentes.menu_superior()

# Verificação de segurança: Apenas administradores
if not st.session_state.get("logado") or st.session_state.get("perfil") != "admin":
    st.error("Acesso restrito a administradores.")
    st.stop()

st.title("🏢 Gestão de Unidades")
st.write("Gerencie as bibliotecas físicas que compõem a rede municipal.")

# Usamos abas para separar o cadastro da visualização
tab_cadastro, tab_lista = st.tabs(["➕ Nova Unidade", "📋 Unidades Ativas"])

# --- ABA 1: FORMULÁRIO DE CADASTRO ---
with tab_cadastro:
    with st.form("form_biblioteca", clear_on_submit=True):
        st.subheader("Dados da Biblioteca")
        
        col1, col2 = st.columns(2)
        with col1:
            nome_unidade = st.text_input("Nome da Unidade", placeholder="Ex: Biblioteca Municipal Vicente Leite")
            responsavel = st.text_input("Responsável/Bibliotecário", placeholder="Nome do encarregado")
            telefone = st.text_input("Telefone de Contato")
        
        with col2:
            endereco = st.text_input("Endereço Completo", placeholder="Rua, Número, Bairro")
            horario = st.text_input("Horário de Funcionamento", placeholder="Ex: Seg a Sex, 08h às 18h")
            capacidade = st.number_input("Capacidade de Acervo (Estimada)", min_value=0, step=100)

        st.write("##")
        enviar = st.form_submit_button("Cadastrar Unidade", type="primary")

        if enviar:
            if nome_unidade and endereco:
                # No futuro, aqui será o POST para o FastAPI
                st.success(f"A unidade '{nome_unidade}' foi integrada à rede Librion!")
                st.balloons()
            else:
                st.error("Por favor, preencha pelo menos o Nome e o Endereço da unidade.")

# --- ABA 2: LISTAGEM ---
with tab_lista:
    st.subheader("Rede de Bibliotecas")
    
    # Simulação de dados (Mock)
    unidades = [
        {"ID": 1, "Unidade": "Biblioteca Central", "Bairro": "Centro", "Livros": 5200, "Status": "Ativa"},
        {"ID": 2, "Unidade": "Biblioteca Pinto Madeira", "Bairro": "Pinto Madeira", "Livros": 2100, "Status": "Ativa"},
        {"ID": 3, "Unidade": "Biblioteca Seminário", "Bairro": "Seminário", "Livros": 1850, "Status": "Em Reforma"},
    ]
    
    # Exibição em DataFrame para permitir ordenação
    st.dataframe(unidades, use_container_width=True, hide_index=True)
    
    st.info("💡 As unidades marcadas como 'Ativa' aparecem como opção no cadastro de livros e catálogo.")