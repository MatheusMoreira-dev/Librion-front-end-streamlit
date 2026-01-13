import streamlit as st
import componentes # Importamos o teu menu superior
import dados        # Importamos a tua lista de livros

# Configuração da página
st.set_page_config(page_title="Librion - Catálogo", layout="wide")

# Exibir o menu superior (que criámos anteriormente)
componentes.menu_superior()

st.title("Catálogo Público")
st.write("Explore o acervo completo da Rede Municipal de Bibliotecas de Crato-CE")

# --- SEÇÃO DE FILTROS ---
# Criamos uma linha com 3 colunas para a pesquisa e os selects
col_busca, col_genero, col_biblio = st.columns([2, 1, 1])

with col_busca:
    termo = st.text_input("🔍 Buscar por título ou autor...", placeholder="Ex: Machado de Assis")

with col_genero:
    genero = st.selectbox("Filtro: Género", ["Todos os géneros", "Romance", "Clássico", "Drama"])

with col_biblio:
    biblioteca = st.selectbox("Filtro: Unidade", ["Todas as bibliotecas", "Centro", "Pinto Madeira", "Seminário"])

st.write(f"**{12} livros encontrados**") # Exemplo estático, pode ser dinâmico com len()
st.write("---")

# --- EXIBIÇÃO EM GRELHA (CARDS) ---
# Vamos simular uma lista de livros (no futuro virá do dados.py ou FastAPI)
lista_livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "local": "Bib. Central", "status": "Disponível"},
    {"titulo": "Grande Sertão", "autor": "Guimarães Rosa", "local": "Bib. Pinto Madeira", "status": "Disponível"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "local": "Bib. Seminário", "status": "Emprestado"},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "local": "Bib. Central", "status": "Disponível"},
    {"titulo": "Memórias Póstumas", "autor": "Machado de Assis", "local": "Bib. Centro", "status": "Disponível"},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "local": "Bib. Muriti", "status": "Disponível"},
]

# Lógica para criar a grelha (3 colunas por linha)
rows = len(lista_livros) // 3 + (1 if len(lista_livros) % 3 > 0 else 0)

for i in range(rows):
    cols = st.columns(3) # Cria 3 colunas para esta linha
    for j in range(3):
        index = i * 3 + j
        if index < len(lista_livros):
            livro = lista_livros[index]
            with cols[j]:
                # Criamos o "Card" usando um container com borda
                with st.container(border=True):
                    # Espaço da Imagem (Placeholder)
                    st.image("https://via.placeholder.com/150x200?text=Livro", use_container_width=True)
                    
                    st.subheader(livro["titulo"])
                    st.caption(f"{livro['autor']}")
                    st.write(f"📍 {livro['local']}")
                    
                    # Linha de botões e status
                    btn_col1, btn_col2 = st.columns([1, 1])
                    with btn_col1:
                        if livro["status"] == "Disponível":
                            st.success("Disponível")
                        else:
                            st.warning("Emprestado")
                    
                    with btn_col2:
                        if st.button("Reservar", key=f"res_{index}"):
                            st.toast(f"Solicitação enviada: {livro['titulo']}")