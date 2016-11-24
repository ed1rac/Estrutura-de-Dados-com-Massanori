dicionario = dict()
dicionario[1] = [6,7]
dicionario[2] = [3,7]
dicionario[3] = [2,6]
dicionario[4] = [3,7]
dicionario[5] = [7]
dicionario[6] = [1,3]
dicionario[7] = [1,2,3,4,5]

dic = dict()
dic[1] = [3]
dic[2] = [3,5]
dic[3] = [1, 2]
dic[4] = [5]
dic[5] = [2, 4] 

diciona = dict()
diciona[1] = [2,6,7,8,11]
diciona[2] = [1,3,12]
diciona[3] = [2,6]
diciona[4] = [6,7]
diciona[5] = [7,8]
diciona[6] = [1,3,4]
diciona[7] = [1,4,7]
diciona[8] = [1,5,9]
diciona[9] = [8,10,11]
diciona[10] = [9]
diciona[11] = [1,9]
diciona[12] = [2]

def removeGuloso(x, item):
    retirar = item[x]
    for atual in item:
        novo = list()
        for j in item[atual]:
            if j not in item[x] and j != x and j not in retirar:
                novo.append(j)
            item[atual] = novo
    for i in retirar:
        item.pop(i)
    item.pop(x)
    return item

def guloso(grafo):
    comp = list()
    while len(grafo) > 1:
        x = localizaGuloso(grafo)
        grafo = removeGuloso(x, grafo)
        comp.append(x)
    if len(grafo) == 1:
        for i in grafo:
            comp.append(i)
    return comp

def localizaGuloso(item):
    menor = len(item)
    for i in item:
        if len(item[i]) < menor:
            escolhido = i
            menor = len(item[i])
    return escolhido

print(dicionario)
print("S = ",guloso(dicionario))
print()
print(dic)
print("S = ",guloso(dic))
print()
print(diciona)
print("S = ",guloso(diciona))
