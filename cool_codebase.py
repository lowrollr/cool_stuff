def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


def add_two_numbers(num1, num2):
    return num1 + num2
