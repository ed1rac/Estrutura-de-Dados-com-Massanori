def inv(s):
    '''Função para inverter um entrada String recursivamente'''
    if len(s) == 1:
        return s
    return inv(s[1:]) + s[0]

print(inv("abc"))
