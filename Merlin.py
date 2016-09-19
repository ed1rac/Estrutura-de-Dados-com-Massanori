def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutações(items):
    return combinações(items, len(items))

def ep2parte1(local):
    '''
    Função achar solução para casamento de damas e cavaleiros
    :param local: endereço ou nome do bloco de notas .txt
    :return: Saida em tela do resultado do exercicio
    '''
    #MANIPULAÇÃO DE ARQUIVOS E TRATAMENTO DE LISTA
    chatas = list()
    noivas = list()
    noivos = list()
    casamento = open(local,'r')
    for i in range(4):
        linha = casamento.readline().split()
        if len(linha) > 1:
            noivos.append(linha[1:])
            noivas.append(linha[:1])
        else:
            noivos.append([])
            chatas.append(linha[:1])
    noivas[0] = [noivas[0][0][3:]]
    casamento.close()

    #PROBLEMAS DE NOIVAS Q NÂO GOSTAM DE NINGUEM
    if len(chatas) > 0: #insuficiencia
        print("As preferencias de",end=' ')
        for i in chatas:
            print(i[0],end=' ')
        print("são insuficientes e")
        return 0

    #CASANDO AS NOIVAS
    novonoivo1 = enumerações(noivos[0])
    for i in range(len(noivos[0])):
        lista = list()
        novo1 = next(novonoivo1)
        novo1 = novo1[-1] #somente item String
        lista.append(novo1) #lista
        novonoivo2 = enumerações(noivos[1])
        for j in range(len(noivos[1])):
            novo2 = next(novonoivo2)
            novo2 = novo2[-1]
            if novo2 in lista:
                continue
            lista.append(novo2)
            novonoivo3 = enumerações(noivos[2])
            for h in range(len(noivos[2])):
                novo3 = next(novonoivo3)
                novo3 = novo3[-1]
                if novo3 in lista:
                    continue
                lista.append(novo3)
                novonoivo4 = enumerações(noivos[3])
                for l in range(len(noivos[3])):
                    novo4 = next(novonoivo4)
                    novo4 = novo4[-1]
                    if novo4 in lista:
                        continue
                    lista.append(novo4)
                    print("Casamento Possível e")
                    return 0
                    lista.pop()
                lista.pop()
            lista.pop()


    #TESTE PARA PROBLEMAS COM NOIVOS
    dicionario = dict()
    for xnoivo in noivos:
        for carinha in xnoivo:
            if carinha not in dicionario.keys():
                dicionario[carinha] = 1
            else:
                dicionario[carinha] += 1
    maximo = max(dicionario.values())
    for i in dicionario.keys():
        if dicionario[i] == maximo:
            for j in range(4):
                if i in noivos[j]:
                    chatas.append(noivas[j])
    print("As preferencias de ",end='')
    for i in chatas:
        print(i[0],' ',end='')
    print("são insuficientes")

def ep2parte2(local):
    #INICIANDO DICIONARIO DE CAVALEIROS
    cavaleiros = dict()
    lista = list()
    #MANIPULANDO ARQUIVO E TRATANDO LISTA
    arquivo = open(local, 'r')
    for i in range(7):
        lista.append(arquivo.readline().split())
    lista[0][0] = lista[0][0][3:]

    #CRIANDO DICIONARIO
    for i in lista:
        cavaleiros[i[0]] = i[1:]
    arquivo.close()
    # CRIANDO GERADOR
    lista = list()
    for i in cavaleiros.keys():
        lista.append(i)
    gerador = permutações(lista)
    #RESOLVENDO
    for permutacao in gerador:
        for indice in range(len(permutacao)-1):
            if permutacao[indice+1] not in cavaleiros[indice]:
                break
            else:

    print("Falso")


ep2parte2("cavaleiros.txt")

