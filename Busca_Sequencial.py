def Busca_Sequencial(seq, buscado):
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