import unittest
from main import livros_em_estoque, Carrinho

class TestLoja(unittest.TestCase):
  def test_adicionar_sucesso(self):
    carrinho = Carrinho()
    
    quantidade = len(carrinho.livros)
    carrinho.adicionar_livro(livros_em_estoque[0])
    
    self.assertGreater(len(carrinho.livros), quantidade)
    self.assertTrue(livros_em_estoque[0] in carrinho.livros)
  
  def test_adicionar_falha(self):
    carrinho = Carrinho()

    quantidade = len(carrinho.livros)
    carrinho.adicionar_livro(livros_em_estoque[0])
    
    self.assertFalse(livros_em_estoque[1] in carrinho.livros)
    self.assertGreater(len(carrinho.livros), quantidade)
  
  def test_remover_sucesso(self):
    carrinho = Carrinho()

    quantidade = len(carrinho.livros)

    carrinho.adicionar_livro(livros_em_estoque[0])
    carrinho.remover_livro(livros_em_estoque[0])
    
    self.assertEqual(len(carrinho.livros), quantidade)

  def teste_remover_falha(self):
    carrinho = Carrinho()
    
    carrinho.adicionar_livro(livros_em_estoque[0])
    quantidade = len(carrinho.livros)
    
    carrinho.remover_livro(livros_em_estoque[1])
    
    self.assertEqual(len(carrinho.livros), quantidade)

    
  def test_limpar_carrinho_sucesso(self):
    carrinho = Carrinho()

    carrinho.adicionar_livro(livros_em_estoque[0])
    quantidade = len(carrinho.livros)

    carrinho.limpar()

    self.assertGreater(quantidade, len(carrinho.livros))
    self.assertFalse(carrinho.livros)
  
  def teste_calcular_valor_total(self):
    carrinho = Carrinho()
    
    carrinho.adicionar_livro(livros_em_estoque[0])
    carrinho.adicionar_livro(livros_em_estoque[1])

    valor_total = carrinho.valor_total()
    valor_esperado = livros_em_estoque[0]['preco'] + livros_em_estoque[1]['preco']
    
    self.assertEqual(valor_total, valor_esperado)