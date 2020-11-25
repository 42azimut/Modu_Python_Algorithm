# P. 60 최대 공약수 구하기! 
# 입력 a, b
# 출력 a,b의 최대 공약수

def gcd(a, b):
    min_num = min(a, b)
    while True:
        if a % min_num == 0 and b % min_num == 0:
            return min_num
        min_num = min_num - 1

print("======gcd 일반 최대 공약수========")
print(gcd(10, 5))
print(gcd(40, 24))
print(gcd(92, 32))
print("======gcd2 유클리드 알고리즘========")

def gcd2(a,b):
    if b == 0:
        return a
    return gcd2(b, a % b)   #gcd(60, 24) = gcd(24, 60 % 24) = gcd(12, 24%12) = gcd(12, 0)

print(gcd2(10, 5))
print(gcd2(40, 24))
print(gcd2(92, 32))

print(60%24, 24%12)
print(81%27)

def gcd3(x, y):
    print("gcd3: ", x, y )
    if y == 0:
        return x
    return (gcd3(y, x%y)) 

print(gcd3(60, 24))
#print(gcd3(24,12))
#print(gcd3(12, 0))