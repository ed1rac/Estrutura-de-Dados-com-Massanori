dicionario = dict()
dicionario[1] = [6,7]
dicionario[2] = [3,7]
dicionario[3] = [2,6]
dicionario[4] = [3,7]
dicionario[5] = [7]
dicionario[6] = [1,3]
dicionario[7] = [1,2,3,4,5]

def removeGuloso(x, item):
    retirar = item[x]
    for atual in dicionario:
        novo = list()
        for j in item[atual]:
            if j not in item[x] and j != x:
                novo.append(j)
            item[atual] = novo
    for i in retirar:
        item.pop(i)
    item.pop(x)
    return item

def guloso(grafo):
    comp = list()
    while len(grafo) != 1:
        x = localizaGuloso(grafo)
        grafo = removeGuloso(x, grafo)
        comp.append(x)
    for i in grafo:
        comp.append(i)
    return comp

def localizaGuloso(item):
    comp = list()
    menor = len(item)
    for i in item:
        if len(item[i]) < menor:
            escolhido = i
            menor = len(item[i])
    return escolhido

print(guloso(dicionario))
print()
print(guloso(dic))
