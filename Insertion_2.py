import unittest

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
    for loop1 in range(0, len(seq)-1):
        top = loop1
        for loop2 in range(loop1+1,len(seq)-1):
            if seq[loop2] < seq[loop1]:
                top = loop2
        seq[loop1], seq[top] = seq[top], seq[loop1]
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_3_elementos(self):
        self.assertListEqual([2, 3, 4], insertion_sort([4, 3, 2]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()