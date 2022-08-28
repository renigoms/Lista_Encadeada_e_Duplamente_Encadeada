# ****************************************
# NO OU CÉLULA
# ****************************************
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


# **************************************************
# LISTA ENCADEADA
# **************************************************


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

    # ******************************************************
    #   BUSCAR VALOR USANDO O INDEX
    # ******************************************************

    def _percorrer(self, perc, count, proximo=True):
        for i in range(count):
            if proximo:
                perc = perc.proximo
            else:
                perc = perc.anterior
        return perc

    def _percorrer_por_index(self, index):
        if index >= self.tamanho or index < 0:
            raise IndexError('Não existe essa posição')
        if index == 0:
            return self.inicio
        elif index == self.tamanho:
            return self.final
        else:
            MetadeTamLista = (self.tamanho - 1) / 2
            count = 0
            proximo = True
            perc = self.inicio
            if index <= MetadeTamLista:
                count = index - 0
            else:
                proximo = False
                count = (self.tamanho - 1) - index
                perc = self.final
            return self._percorrer(perc, count, proximo)

    def buscar_valor_pelo_index(self, index):
        perc = self._percorrer_por_index(index)
        return perc.valor

    # ******************************************************
    #   BUSCAR INDEX USANDO O VALOR
    # ******************************************************

    def _percorrer_os2lados_count(self, valor, perc_inicial, perc_final, metade, count_inicial, count_final,
                                  impar=True):
        if impar:
            while perc_inicial.valor is not perc_final.valor:
                if perc_inicial.valor == valor:
                    return count_inicial
                elif perc_final.valor == valor:
                    return count_final
                perc_inicial = perc_inicial.proximo
                perc_final = perc_final.anterior
                count_inicial += 1
                count_final -= 1
            ValorMeio = self.buscar_valor_pelo_index(metade)
            if ValorMeio == valor:
                return metade
            else:
                raise Exception('VALOR NÃO ESTÁ NA LISTA')
        else:
            while count_inicial is not metade and count_final != metade + 1:
                if perc_inicial.valor == valor:
                    return count_inicial
                elif perc_final.valor == valor:
                    return count_final
                perc_inicial = perc_inicial.proximo
                perc_final = perc_final.anterior
                count_inicial += 1
                count_final -= 1
            ValorMeio_inicial = self.buscar_valor_pelo_index(metade)
            ValorMeio_final = self.buscar_valor_pelo_index(metade + 1)
            if ValorMeio_inicial == valor:
                return metade
            elif ValorMeio_final == valor:
                return metade + 1
            else:
                raise Exception('VALOR NÃO ESTÁ NA LISTA')

    def _percorrer_por_valor(self, valor):
        if self.tamanho == 0:
            raise IndexError('NÃO EXISTE ELEMENTOS NA LISTA')
        count = 0
        count2 = self.tamanho - 1
        if valor == self.inicio.valor:
            return count
        elif valor == self.final.valor:
            return count2
        else:
            if self.tamanho % 2 == 0:
                perc_inicial = self.inicio
                perc_final = self.final
                metade = int((self.tamanho - 1) / 2)
                TamListaImpar = False
            else:
                perc_inicial = self.inicio
                perc_final = self.final
                metade = int((self.tamanho - 1) / 2)
                TamListaImpar = True
            return self._percorrer_os2lados_count(valor, perc_inicial, perc_final, metade, count, count2,
                                                  TamListaImpar)

    def buscar_index_pelo_valor(self, valor):
        count = self._percorrer_por_valor(valor)
        return count

    # ADICIONAR ELEMENTOS SEMPRE AO FINAL DA LISTA

    def adicionar(self, valor):
        no = _No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.final = no
        else:
            self.final.proximo = no
            no.anterior = self.final
            self.final = no

        self.tamanho += 1

    def inserir(self, index, valor):
        if self.tipo and type(valor) != self.tipo:
            raise TypeError(f'Tipo inválido, a função só aceita tipo: {self.tipo}')
        if index >= self.tamanho:
            self.adicionar(valor)
            return
        no = _No(valor)
        if index == 0:
            no.proximo = self.inicio
            self.inicio = no
            self.tamanho += 1

        elif index > self.tamanho - 1:
            self.final.proximo = no
            no.anterior = self.final
            no.proximo = None
            self.final = no
            self.tamanho += 1

        else:
            metade = (self.tamanho - 1) / 2
            if index <= metade:
                perc_inicial = self.inicio
                perc_inserir1 = self._percorrer(perc_inicial, index - 1)
                no.proximo = perc_inserir1.proximo
                perc_inserir1.proximo.anterior = no
                perc_inserir1.proximo = no
                no.anterior = perc_inserir1
                self.tamanho += 1
            else:
                perc_final = self.final
                indexDetrasPfrente = (self.tamanho - 1) - index - 1
                perc_inserir2 = self._percorrer(perc_final, indexDetrasPfrente, False)
                no.anterior = perc_inserir2.anterior
                perc_inserir2.anterior.proximo = no
                perc_inserir2.anterior = no
                no.proximo = perc_inserir2
                self.tamanho += 1

    # ***********************************************
    #           EDITAR ITENS
    # ***********************************************

    def editar_item(self, index, novo_valor):
        perc = self._percorrer_por_index(index)
        perc.valor = novo_valor

    # ***********************************************
    #           REMOVER ITENS
    # ***********************************************
    def remover_item(self, valor):
        if self.tamanho == 0:
            raise Exception('Não há itens na lista')
        perc_inicio = self.inicio
        perc_final = self.final
        if perc_inicio.valor == valor:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        elif perc_final.valor == valor:
            self.final = self.final.anterior
            self.final.proximo = None
            self.tamanho -= 1

        else:
            indexvalor = self.buscar_index_pelo_valor(valor)
            self.remover_index(indexvalor)

    # ***********************************************
    #           REMOVER ITENS 1-->2-->3-->4
    # ***********************************************
    def remover_index(self, index):
        # print((self.tamanho-1)-index+1)

        if index >= self.tamanho or index < 0:
            raise IndexError('Não existe essa posição')
        elif index == 0:
            self.inicio = self.inicio.proximo
        elif index == self.tamanho - 1:
            self.final = self.final.anterior
            self.final.proximo = None
            self.tamanho -= 1
        else:
            metade = int(self.tamanho - 1) / 2
            if index <= metade:
                perc_inicio = self.inicio
                perc = self._percorrer(perc_inicio, index - 1)
                aux = perc.proximo
                perc.proximo = aux.proximo
                aux.proximo.anterior = perc
                aux = None
                self.tamanho -= 1
            else:
                perc_final = self.final
                indexDtrasPfrente = (self.tamanho - 1) - index
                perc2 = self._percorrer(perc_final, indexDtrasPfrente - 1, False)
                aux = perc2.anterior
                perc2.anterior = aux.anterior
                aux.anterior.proximo = perc2
                aux = None
                self.tamanho -= 1

    def buscar_valores_repetidos(self):
        pass

    def ordenar(self, crescente=True):
        pass


# ******************************************************
# ÁREA DE TESTES
# ******************************************************

lista = ListEncaDupla()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.inserir(0, 20)
lista.inserir(1, 22)
lista.inserir(2, 23)
lista.inserir(3, 24)
lista.inserir(4, 25)
lista.remover_item(4)
lista.remover_index(3)

print(len(lista))
print(lista)
