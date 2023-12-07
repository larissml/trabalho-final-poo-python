from Produto import Produto
class Livros(Produto):
    __slots__ = "__titulo", "__autor"
    def __init__(self, titulo, autor, codigo, valor):
        super().__init__(codigo, valor)
        self.__titulo = titulo
        self.__autor = autor
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, novoTitulo):
        self.__titulo = novoTitulo
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, novoAutor):
        return self.__autor
    def calculaDesconto(self):
        return super().valor * 0.95
    def detalhes(self):
        det ="-------- LIVRO --------\n"
        det += "Título: " + self.__titulo + "\n"
        det+="Autor: " + self.__autor +"\n"
        det+= super().__str__() + "\n"
        det+= "Desconto: 5%"
        return det