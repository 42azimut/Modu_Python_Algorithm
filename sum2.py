#1부터 n까지 연속된 숫자의 합을 구하시오! 앞의 sum.py보다 나은 알고리즘!

def sum(n):
    return n * (n +1) // 2  #// 는 정수 나눗셈!

print(sum(10))
print(sum(1000))