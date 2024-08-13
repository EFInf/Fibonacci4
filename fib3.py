# Top-down (Rekursion) mit Memoisation

results = [0,1]
def fib3(n):
    if n<len(results):
        return results[n]
    else:
        results.append(n,fib3(n-2)+fib3(n-1))
        return results[n]
    
print(fib3(10))
print(results)