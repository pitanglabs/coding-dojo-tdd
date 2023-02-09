livros_em_estoque = [
  {'id': 1, 'nome': "Livro Invisível da Invisibilidade", 'preco': 10},
  {'id': 2, 'nome': "O Livro Monstruoso dos Monstros", 'preco': 3},
  {'id': 3, 'nome': "A Vida e as Mentiras de Alvo Dumbledore", 'preco': 5},
  {'id': 4, 'nome': "Viagens com Trasgos", 'preco': 2},
  {'id': 5, 'nome': "Hogwarts: Uma História", 'preco': 2},
  {'id': 6, 'nome': "Segredos das Artes das Trevas", 'preco': 5},
  {'id': 7, 'nome': "Trouxas Sensitivos", 'preco': 1},
  {'id': 8, 'nome': "Quadribol Através dos Séculos", 'preco': 5},
]

class Carrinho:
  def __init__(self) -> None:
    self.livros = []

  def adicionar_livro(self, livro):
    self.livros.append(livro)
  
  def remover_livro(self, livro):
    if livro in self.livros:
      self.livros.remove(livro)
  
  def limpar(self):
    self.livros = []
  
  def valor_total(self):
    return sum(map(lambda l: l['preco'], self.livros))