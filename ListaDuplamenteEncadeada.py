class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        proximo = f' ,{self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'


class ListEncaDupla:
    def __init__(self, tipo=None):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tipo = tipo

    def __str__(self):
        return f'[{self.inicio}]'

    def __len__(self):
        return self.tamanho

    def _percorrer(self,perc,cont,proximo):
        pass

    def _get_perc_index(self, index):
        pass

    def _get_perc_valor(self,valor):
        pass

    def _get_valor(self,valor):
        pass

    def _get_index(self, index):
        pass

    def adicionar(self,valor):
        pass

    def inserir(self,index, valor):
        pass

    def editar_item(self, index, novo_valor):
        pass

    def remover_item(self):
        pass

    def remover_index(self, index):
        pass

    def buscar_valores_repetidos(self):
        pass

    def ordenar(self, crescente=True):
        pass


