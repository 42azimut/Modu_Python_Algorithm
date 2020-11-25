# 입력 리스트 a, 찾는값 x
# 출력 : 특정 숫자를 찾으면 그 값의 인덱스 못찾으면 -1

def binary_search_recursion(a, x, start, end):
    #종료조건 : 남은 탐색 범위가 비었으면 종료!
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_recursion(a, x, mid + 1, end)
    else:
        return binary_search_recursion(a, x, start, mid - 1)

    return -1

def binary_search(a, x):
    return binary_search_recursion(a, x, 0, len(a) -1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36)) 
print(binary_search(d, 50))

