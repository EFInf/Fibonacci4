# Bottom-up (Schleife)

def fib1(n):
    a, b = 0, 1
    for _ in range(2,n+1):
        a, b = b, a+b
    return b

print(fib1(10))