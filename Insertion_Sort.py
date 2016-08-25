import unittest
from random import shuffle


def insertion_sort(seq):
    '''
    Função tem como entrada uma lista de numeros e retorna
    a mesma lista organizada, faz iteração de n-1 em n vezes.
    Função tem tempo em O(n**2) e espaço O(1)
    :param seq: lista como numeros
    :return seq: retorna mesma lista organizada por valor
    '''
    if len(seq) <= 1:
        return seq
    local = 1
    for i in range(1, len(seq)+1):
        local = i - 1;
        while local != 0:
            if seq[local] < seq[local-1]:
                seq[local], seq[local-1] = seq[local-1], seq[local]
            local -= 1
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_2000(self):
        lista1 = list(range(2000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))


'''    def teste_lista_4000(self):
        lista1 = list(range(4000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))


    def teste_lista_6000(self):
        lista1 = list(range(6000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))


    def teste_lista_8000(self):
        lista1 = list(range(8000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))


    def teste_lista_10000(self):
        lista1 = list(range(10000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))


    def teste_lista_18000(self):
        lista1 = list(range(18000))
        lista2 = lista1
        shuffle(lista2)
        self.assertListEqual(lista1, insertion_sort(lista2))
'''
if __name__ == '__main__':
    unittest.main()
