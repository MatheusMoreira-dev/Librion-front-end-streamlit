import streamlit as st
import componentes

# 1. Configuração da página
st.set_page_config(page_title="Librion - Minha Conta", layout="wide")
componentes.menu_superior()

# Verificação de segurança: Usuário precisa estar logado
if not st.session_state.get("logado"):
    st.error("Por favor, faça login para acessar esta página.")
    st.button("Ir para Login", on_click=lambda: st.switch_page("pages/2_Login.py"))
    st.stop()

# --- LÓGICA DE TROCA DE SENHA OBRIGATÓRIA ---
if st.session_state.get("primeiro_acesso", True):
    st.warning("⚠️ **Segurança:** Detectamos que este é seu primeiro acesso. Altere sua senha para continuar.")
    with st.container(border=True):
        nova_senha = st.text_input("Nova Senha", type="password")
        confirma = st.text_input("Confirmar Nova Senha", type="password")
        if st.button("Salvar e Acessar Conta", type="primary"):
            if nova_senha == confirma and len(nova_senha) >= 6:
                st.session_state.primeiro_acesso = False
                st.success("Senha alterada! Carregando seu perfil...")
                st.rerun()
            else:
                st.error("As senhas não coincidem ou são muito curtas.")
    st.stop() # Interrompe a página aqui até a senha ser trocada

# --- PERFIL DO USUÁRIO ---
col_av, col_info = st.columns([1, 8])
with col_av:
    # Simulação de Avatar com as iniciais
    st.markdown(f"<div style='background-color:#456e7d; color:white; border-radius:50%; width:80px; height:80px; display:flex; align-items:center; justify-content:center; font-size:30px;'>{st.session_state.nome_usuario[0]}</div>", unsafe_allow_html=True)

with col_info:
    st.subheader(st.session_state.get("nome_usuario", "Usuário"))
    st.caption("📍 Biblioteca de Referência: Biblioteca Central Raimundo Alencar Pinto")

st.write("##")

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

# --- NAVEGAÇÃO INTERNA (TABS) ---
tab_acervo, tab_emprestimos, tab_reco = st.tabs(["📚 Meu Acervo", "📑 Meus Empréstimos", "✨ Recomendações"])

with tab_emprestimos:
    st.markdown("### Histórico de Empréstimos")
    st.write("Acompanhe seus empréstimos ativos e histórico.")
    
    # Exemplo de livro ativo
    with st.container(border=True):
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            st.markdown("**Dom Casmurro**")
            st.caption("Machado de Assis")
            st.write("📅 Empréstimo: 2025-10-01 | Devolução: 2025-10-15")
        with c2:
            st.info("Ativo")
        with c3:
            st.button("Renovar", key="renovar_1")

    # Exemplo de livro atrasado
    with st.container(border=True):
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            st.markdown("**A Moreninha**")
            st.caption("Joaquim Manuel de Macedo")
            st.write("📅 Empréstimo: 2025-09-20 | Devolução: 2025-10-04")
        with c2:
            st.error("Atrasado")
        with c3:
            st.button("Renovar", key="renovar_2", disabled=True)