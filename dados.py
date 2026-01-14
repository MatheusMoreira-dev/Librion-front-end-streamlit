# Ficheiro: dados.py

def buscar_livros():
    """Retorna a lista completa de livros."""
    return [
        {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
        {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977},
        {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988},
        {"titulo": "Grande Sertão: Veredas", "autor": "Guimarães Rosa", "ano": 1956},
        {"titulo": "Memórias Postumas", "autor": "Machado de Assis", "ano": 1881}
    ]

def filtrar_por_termo(lista_livros, termo):
    """Filtra a lista baseada num termo de pesquisa."""
    if not termo:
        return lista_livros
    
    termo = termo.lower()
    resultado = [
        livro for livro in lista_livros 
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower()
    ]
    return resultado