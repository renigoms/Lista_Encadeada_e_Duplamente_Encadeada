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
        pass

    # ***********************************************
    #           EDITAR ITENS
    # ***********************************************

    def editar_item(self, index, novo_valor):
        perc = self._percorrer_por_index(index)
        perc.valor = novo_valor

    def remover_item(self, valor):
        if self.tamanho == 0:
            raise Exception('LISTA VAZIA')
        pass

    def remover_index(self, index):
        pass

    def buscar_valores_repetidos(self):
        pass

    def ordenar(self, crescente=True):
        pass


# ******************************************************
# ÁREA DE TESTES
# ******************************************************

lista_dupla = ListEncaDupla()
lista_dupla.adicionar(10)
lista_dupla.adicionar(40)
lista_dupla.adicionar(90)
lista_dupla.adicionar(60)
lista_dupla.adicionar(220)
lista_dupla.adicionar(70)
lista_dupla.adicionar(75)
lista_dupla.editar_item(1,55)

print(lista_dupla)
print(lista_dupla.buscar_index_pelo_valor(60))
