# 리스트에서 특정 숫자 "위치(인덱스)" 찾기
# 입력 리스트a, 찾는값 x
# 출력 찾으면 그 인덱스, 못찾으면 -1

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if (x == a[i]):
            return i
    return -1



v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 142))


