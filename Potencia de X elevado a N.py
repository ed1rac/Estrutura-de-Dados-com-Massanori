def potencia(n, x):
    if x <= 0:
        return 1
    return n * potencia(n, x-1)
