from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
    
