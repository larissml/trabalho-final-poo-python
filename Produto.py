import abc
class Produto(abc.ABC):
    __slots__ = "__codigo", "__valor" 
    def __init__(self, codigo, valor):
        self.__codigo = codigo
        self.__valor = valor
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, novoCodigo):
        self.__codigo = novoCodigo
    @property
    def valor (self):
        return self.__valor       
    @valor.setter
    def valor(self, novoValor):
        self.__valor = novoValor
    def __str__(self):
        ret = "Código: " + self.__codigo + "\n"
        ret += "Valor: R$" + self.__formataReal(self.__valor)
        return ret
    @abc.abstractmethod
    def calculaDesconto (self):
        pass
    @abc.abstractmethod
    def detalhes(self):
        pass
    def __formataReal(self, valor):
        valorStr= str("%.2f"%valor)
        return valorStr.replace(".",",")

