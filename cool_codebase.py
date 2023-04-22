def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
