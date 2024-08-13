# Top-down (Rekursion)

def fib2(n):
    if n<=1:
        return n
    else:
        return fib2(n-2)+fib2(n-1)
    
print(fib2(10))