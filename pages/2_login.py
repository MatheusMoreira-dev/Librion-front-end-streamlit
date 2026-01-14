import streamlit as st
import componentes

# Configuração da página para esconder a barra lateral e focar no login
st.set_page_config(page_title="Librion - Login", layout="wide", initial_sidebar_state="collapsed")

# Exibir o menu superior (que criámos anteriormente)
componentes.menu_superior()

def validar_login(email, senha):
    """
    Simulação do Back-end (FastAPI). 
    No futuro, esta função fará um pedido HTTP (requests.post).
    """
    if email == "admin@librion.com" and senha == "123":
        return {"sucesso": True, "perfil": "admin", "nome": "Administrador"}
    elif email == "leitor@email.com" and senha == "123":
        return {"sucesso": True, "perfil": "leitor", "nome": "João Leitor"}
    else:
        return {"sucesso": False, "mensagem": "E-mail ou senha incorretos."}

# --- INTERFACE ---
# Criamos margens nas laterais para centralizar o conteúdo [Coluna Vazia, Conteúdo, Coluna Vazia]
_, centro, _ = st.columns([1, 4, 1])

with centro:
    # Dividimos o centro em duas colunas: Imagem/Boas-vindas e Formulário
    col_img, col_form = st.columns([1, 1], gap="large")

    # COLUNA DA ESQUERDA (Visual)
    with col_img:
        with st.container(border=True): # Simula o card azul da imagem
            st.image("https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1000", caption="Bem-vindo ao Librion")
            st.markdown("### Faça parte da rede integrada de bibliotecas municipais de Crato-CE")

    # COLUNA DA DIREITA (Login)
    with col_form:
        st.subheader("Acesse sua conta")
        st.write("Entre com suas credenciais para acessar o Librion")
        
        email = st.text_input("E-mail", placeholder="seu@email.com")
        senha = st.text_input("Senha", type="password", placeholder="********")
        
        st.caption("Esqueci minha senha")
        
        if st.button("Fazer Login", type="primary", use_container_width=True):
            resultado = validar_login(email, senha)
            
            if resultado["sucesso"]:
                # 1. Guardamos as informações na "Memória de Curto Prazo" (Session State)
                st.session_state.logado = True
                st.session_state.perfil = resultado["perfil"]
                st.session_state.nome_usuario = resultado["nome"]

                # 2. Definimos se é o primeiro acesso (para forçar troca de senha depois)
                 # No futuro, o seu back-end dirá se é True ou False
                st.session_state.primeiro_acesso = True
                
                st.success(f"Bem-vindo, {resultado['nome']}!")
                
                # Lógica de redirecionamento:
                if resultado["perfil"] == "admin":  
                    st.switch_page("pages/4_Admin_Livros.py") # Vai direto para o cadastro
                else:
                    st.switch_page("pages/7_Minha_Conta.py") # Leitor vai para a página dele
            else:
                st.error(resultado["mensagem"])

# Botão para voltar sem logar
if st.button("← Voltar para a Início"):
    st.switch_page("Home.py")