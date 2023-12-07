from Produto import Produto
class Revistas(Produto):
    __slots__ = "__nome", "__anoPublicacao"
    def __init__(self, codigo, valor, nome, anoPublicacao):
        super().__init__(codigo, valor)
        self.__nome = nome
        self.__anoPublicacao = anoPublicacao
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    @property
    def anoPublicacao(self):
        return self.__anoPublicacao
    @anoPublicacao.setter
    def anoPublicacao(self, novoAno):
        self.__anoPublicacao = novoAno
    def calculaDesconto (self):
        return super().valor * 0.85
    def detalhes(self):
        det ="-------- REVISTA --------\n"
        det+= "Nome: " + self.__nome + "\n"
        det+="Ano publicação: " + self.__anoPublicacao+"\n"
        det+= super().__str__() + "\n"
        det+= "Desconto: 15%"
        return det