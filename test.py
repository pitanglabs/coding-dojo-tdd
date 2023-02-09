import unittest
from main import livros_em_estoque, Carrinho

class TestLoja(unittest.TestCase):
  def test_adicionar(self):
    carrinho = Carrinho()
    
    quantidade = len(carrinho.livros)
    livros = carrinho.adicionar_livro(livros_em_estoque[0])
    self.assertEqual(len(livros), quantidade + 1)

  def test_remover(self):
    raise NotImplementedError