from functools import lru_cache

@lru_cache(maxsize=None)
def fibonati(n):
    print(n)
    if n <= 2:
        return 1
    return fibonati(n-2) + fibonati(n-1)
