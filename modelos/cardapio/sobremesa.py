from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return f"Sobremesa: {self._nome} - R$ {self._preco:.2f}"
    
    def aplicar_desconto(self, percentual):
        desconto = self._preco * (percentual / 100)
        self._preco -= desconto
        return self._preco