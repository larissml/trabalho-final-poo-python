from Jornais import Jornais
from Livros import Livros
from Revistas import Revistas
from CarrinhoDeCompras import CarrinhoDeCompras
jornal = Jornais("Gazeta","123",10,"20/10/1098")
livro = Livros("Harry P.","JK ROWLING", "1158", 60)
revista =  Revistas("178",5, "Caras","2000")
carrinho = CarrinhoDeCompras()
carrinho.registra(jornal)
carrinho.registra(livro)
carrinho.registra(revista)
carrinho.detalheCarrinho()

#TESTE PARA HASATTR E TRATAMENTO DE EXCEÇÃO
#carrinho = CarrinhoDeCompras()
#carrinho.registra("livro")
#carrinho.detalheCarrinho()