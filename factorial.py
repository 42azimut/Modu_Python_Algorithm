#연속한 숫자의 곱을 구해라
# 입력 n , 출력 : 1부터 n까지의 연속한 숫자의 곱!

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num = num * i
    return print(num)

factorial(10)
factorial(4)




