def fibonacci(n):
    d = {1: 1, 2: 1}
    if n in d:
        return d[n]
    else:
        d[n] = fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))
