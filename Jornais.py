from Produto import Produto
class Jornais(Produto):
    __slots__ = ("__nome", "__dataPublicacao")
    def __init__(self, nome, codigo, valor, dataPublicacao):
        super().__init__(codigo, valor)
        self.__dataPublicacao = dataPublicacao
        self.__nome = nome
    @property
    def dataPublicacao(self):
        return self.__dataPublicacao
    @dataPublicacao.setter
    def dataPublicacao(self, novaData):
        self.__dataPublicacao = novaData
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    def calculaDesconto (self):
        return super().valor * 0.90
    def detalhes(self):
        det="-------- JORNAL --------\n"
        det+= "Nome: " + self.__nome + "\n"
        det+= super().__str__() + "\n"
        det+= "Data publicação: " + self.__dataPublicacao
        det+= "\nDesconto: 10%"
        return det