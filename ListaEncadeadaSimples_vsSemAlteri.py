class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __str__(self):
        proximo = f', {self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __str__(self):
        return f'[{self.inicio}]'

    def __len__(self):
        return self.tamanho

    def adicionaritens(self, valor):

        no = _No(valor)
        if not self.inicio:

            self.inicio = no
        else:
            perc = self.inicio
            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = no
        self.tamanho += 1

    def inseriritem(self, index, valor):
        no = _No(valor)  # adiciona o parâmetro valor ao nó
        if index >= self.tamanho:  # pro final
            self.adicionaritens(valor)
            return

        elif index == 0:  # pro inicial
            no.proximo = self.inicio
            # o no.proximo vai apontar para o self.inicio,
            # que é a caixinha inicial
            self.inicio = no
            # logo após irá depositar o valor nó com self.inicio = no
        else:
            perc = self.inicio
            for i in range(index - 1):
                perc = perc.proximo
            no.proximo = perc.proximo
            perc.proximo = no
        self.tamanho += 1

    def remover_index(self, index):
        if index > self.tamanho:
            raise Exception('Não há um item na lista com esse index')
        perc = self.inicio
        for i in range(index - 1):
            perc = perc.proximo
        perc.proximo = perc.proximo.proximo
        self.tamanho -= 1

    def remover_item(self, valor):
        pass

    def get_index(self, index):
        if self.tamanho == 0:
            raise IndexError('NÃO EXISTE ELEMENTOS NA LISTA')
        perc = self.inicio
        for i in range(index):
            perc = perc.proximo
        return perc.valor

    def editar_item(self, index, novo_valor):
        if self.tamanho == 0:
            raise IndexError('Não há itens para serem editados na lista')
        perc = self.inicio
        for i in range(index):
            perc = perc.proximo
        perc.valor = novo_valor

    def buscar_valores_repetidos(self):
        pass


lista2 = Lista()
lista2.adicionaritens(15)
lista2.adicionaritens(15)
lista2.adicionaritens(15)
lista2.adicionaritens(15)
lista2.inseriritem(1000, 500)
print(lista2)
