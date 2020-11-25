#피보나치 수열

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:            
            return fibo(n - 2) + fibo(n -1)


print(fibo(10))
print(fibo(1), fibo(0), fibo(2))

list_fibo = []
for i in range(20):
    list_fibo.append(fibo(i))
print(list_fibo)
    