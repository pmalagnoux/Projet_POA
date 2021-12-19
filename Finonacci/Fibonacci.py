def fib(n):
    x = 0
    y = 1
    for i in range(1, n):
        z = (x + y)
        x = y
        y = z
    return y


if __name__ == '__main__':
    for _ in range(1000000):
        print(fib(92))
