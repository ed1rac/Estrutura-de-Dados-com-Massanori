def mdc(a, b, n):
    '''Função achar o minimo divisor comum em inteiros a e b'''
    if a % n == 0 and b %n==0:
        return n
    return mdc(a , b, n + 1)

print(mdc(10,5, 2))
print(mdc(20, 42 , 2))
