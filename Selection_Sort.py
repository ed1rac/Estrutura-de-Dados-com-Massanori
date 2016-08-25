import unittest
from random import shuffle

def selection_sort(seq):
    '''
    Função tem como entrada uma lista de numeros e retorna
    a mesma lista organizada, faz iteração de n-1 em n vezes.
    Função tem tempo em O(n**2) e espaço O(1)
    :param seq: lista como numeros
    :return seq: retorna mesma lista organizada por valor
    '''
    tam = len(seq)
    if tam == 0 or tam == 1:
        return seq
    cont = 1
    i = 0
    while i < tam:
        menor = i
        while cont < tam:
            if seq[menor] > seq[cont]:
                menor = cont
            cont += 1
        seq[i], seq[menor] = seq[menor], seq[i]
        i += 1
        cont = i + 1
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], selection_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], selection_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], selection_sort([2, 1]))

    def teste_lista_3_elementos(self):
        self.assertListEqual([2, 3, 4], selection_sort([4, 3, 2]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], selection_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


    def teste_lista_2000(self):
        lista1 = list(range(2000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, selection_sort(lista2))


if __name__ == '__main__':
    unittest.main()