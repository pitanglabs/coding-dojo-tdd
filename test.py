import unittest

from main import Carrinho

class TesteLivraria(unittest.TestCase):
    def test_adicionar_livro(self):
        carrinho = Carrinho()
        livro = 'a pedra filosofal'
        result_adicionar = carrinho.adicionar_livro(livro)
        self.assertTrue(result_adicionar)