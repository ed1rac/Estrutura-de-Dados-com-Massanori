__author__ = "Sham Vinicius Fiorin"
from time import time
from random import sample
from random import choice
def busca_sequencial(seq, buscado):
    '''
    Função tem como entrada lista de
    :param seq: lista desordenada
    :param buscado: numero buscado
    :return: indice do numero buscado
    '''
    i = 0
    for item in seq:
        if item == buscado:
            return i
        i += 1
    return -1
def busca_binaria(seq, procurado):
    """
    Deve retornar o índice onde o elemento deveriar ser inserido em lista ordenada
    Programa Tem caracteristicas de Tempo em O(N log(N)) e Espaço em O(1)
    :param procurado: elemento a ser procurado
    :param seq: sequencia a ser pesquisada
    :return: int
    """
    inicio = 0
    final = len(seq)
    while final > inicio:
        meio = (inicio + final) // 2
        if procurado <= seq[meio]:
            final = meio
        else:
            inicio = meio + 1
    return final
def insertion_sort(seq):
    '''
    Função tem como entrada uma lista de numeros e retorna
    a mesma lista organizada, faz iteração de n-1 em n vezes.
    Função tem tempo em O(n**2) e espaço O(1)
    :param seq: lista como numeros
    :return seq: retorna mesma lista organizada por valor
    '''
    for j in range(1, len(seq)):
        x = seq[j]
        i = j - 1
        while i >= 0 and seq[i] > x:
            seq[i + 1] = seq[i]
            i -= 1
        seq[i + 1] = x
    return seq
def selection_sort(seq):
    '''
    Função tem como entrada uma lista de numeros e retorna
    a mesma lista organizada, faz iteração de n-1 em n vezes.
    Função tem tempo em O(n**2) e espaço O(1)
    :param seq: lista como numeros
    :return seq: retorna mesma lista organizada por valor
    '''
    lista = []
    while len(seq) > 0:
        m = min(seq)
        lista.append(m)
        seq.remove(m)
    return lista
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r
def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)
def quick_sort(lista):
    try:
        if len(lista) <= 1:
            return lista

        pivô = lista[0]
        iguais = [x for x in lista if x == pivô]
        menores = [x for x in lista if x < pivô]
        maiores = [x for x in lista if x > pivô]
        return quick_sort(menores) + iguais + quick_sort(maiores)
    except RuntimeError:
        RuntimeError
    except TypeError:
        TypeError
def ordenando(n, tipo):
    lista = sample(list(range(30000)), n)
    lst = lista
    dic = {0: insertion_sort, 1: selection_sort, 2: mergesort, 3: quick_sort}
    ini = time()
    dic[tipo](lst)
    fim = time()
    tempo = fim-ini
    return tempo, buscando(tempo, lst ,n ,lista)
def buscando(tempo, lista, n, original):
    sequencial = 0
    busca = 0
    while sequencial <= tempo:
        # binaria
        if not len(lista):
            original = sample(list(range(30000)), n)
            lista = quick_sort(original)
        escolhido = choice(lista)
        ini = time()
        busca_binaria(lista, escolhido)
        fim = time()
        tempo += (fim - ini)
        busca += 1
        # sequencial
        ini = time()
        busca_sequencial(original, escolhido)
        fim = time()
        sequencial += (fim - ini)
    return busca
def ep1(tempototal):
    '''Algoritmo printa na tela EP 1  - Vale Apena Ordenar?
    :param tempototal: Tempo total de execução do algoritmo
    :return:
    '''
    print('''
    |-------------------------[EP1 - Vale a pena ordenar?]--------------------|
    |  Credito: SHAM VINICIUS FIORIN    -    ADS  -   FATEC                   |
    |            Tempos de Ordenacao            Numeros de Buscas Binarias    |
    |-------------------------------------------------------------------------|
    |   n   | Insercao Selecao Merge  Quick  | Insercao Selecao Merge  Quick  |
    |-------|-----------------------------------------------------------------|''')
    relogio = 0
    n = 2000
    while relogio < tempototal:
        ini = time()
        buscas = list()
        tempos = list()
        for i in range(4):
            t, busca = ordenando(n, i)
            tempos.append(t)
            buscas.append(busca)
        fim = time()
        relogio += (fim-ini)
        print("    |   %i|   %.2f    %.2f   %.2f   %.2f       %i    %i    %i    %i   |"
              % (n , tempos[0], tempos[1], tempos[2], tempos[3], buscas[0], buscas[1], buscas[2], buscas[3]))
        n += 2000
    print("Tempo total dos testes: %.1f" %tempototal)

