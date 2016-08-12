def sd(n):
    print(n)
    '''Exercicio Soma de Digitos de um inteiro Recursivo'''
    if n//10 == 0:
        return n
    return n%10 + sd(n//10)

print(sd(123),"resposta 6")
print(sd(122),"resposta 5")
print(sd(111),"resposta 3")
