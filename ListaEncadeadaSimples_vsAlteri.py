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
    def __init__(self, tipo=None):

        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tipo = tipo

    def __str__(self):
        return f'[{self.inicio}]'

    def __len__(self):
        return self.tamanho

    def __getitem__(self, item):
        return self.get_valor(item)

    def adicionaritens(self, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        no = _No(valor)
        if not self.final:
            self.final = no
            self.inicio = no
        else:
            self.final.proximo = no
            self.final = no
        self.tamanho += 1

    def inseriritem(self, index, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if index >= self.tamanho:  # pro final
            self.adicionaritens(valor)
            return
        no = _No(valor)  # adiciona o parâmetro valor ao nó
        if index == 0:  # pro inicial
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

    def get_valor(self, index):
        if self.tamanho == 0:
            raise IndexError('NÃO EXISTE ELEMENTOS NA LISTA')
        if index == self.tamanho:
            return self.final.valor
        perc = self.inicio
        for i in range(index):
            perc = perc.proximo
        return perc.valor

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


lista = Lista()
lista.adicionaritens(1)
lista.adicionaritens(2)
lista.adicionaritens(3)

lista.inseriritem(3, 4)
lista.inseriritem(4, 5)
lista.editar_item(4, 6)
lista.adicionaritens(54)
lista.adicionaritens(55)
lista.remover_index(4)
lista.remover_index(3)
lista.adicionaritens(6)
lista.adicionaritens(6)
print(lista.get_valor(3))
print(lista.get_index(4))


print(len(lista))

print(lista)
