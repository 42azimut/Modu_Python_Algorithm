# 1부터 n까지 "연속한"한 숫자의 합을 구하는 알고리즘!
#입력 n
#출력 1부터 n까지의 더한 값!

def sum(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

print(sum(10))
print(sum(100))