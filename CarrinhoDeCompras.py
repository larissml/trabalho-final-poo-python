from Revistas import Revistas
from Jornais import Jornais
from Livros import Livros
class CarrinhoDeCompras:
    def __init__(self, totalCompra=0):
        self.__totalCompra = totalCompra
        self.__produtos = []
    def registra (self, obj):
            self.__produtos.append(obj)
            if (hasattr(obj, "calculaDesconto")):                 
                self.__totalCompra+= obj.calculaDesconto()
            else: 
                print("O objeto não possui o atributo calculaDesconto")
    def detalheCarrinho(self):
        try:
            for produto in self.produtos:
                print(produto.detalhes())
            ret="---------------------\n"
            ret += "Valor total carrinho: R$ " + str("%.2f"%self.__totalCompra).replace(".",",")
            print(ret)
        except AttributeError:
            print("Erro ao detalhar o carrinho, verifique os produtos.")
    @property
    def totalCompra(self):
        return self.__totalCompra
    @property
    def produtos(self):
        return self.__produtos