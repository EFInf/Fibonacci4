# Bottom-up (Schleife), mit Memoisation

result = [0,1]

def fib4(n): 
    for _ in range(len(result),n+1):
        result.append(result[-2]+result[-1])
    return result[n]

print(fib4(10))
print(result)