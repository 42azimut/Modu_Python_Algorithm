#삽입 정렬 일반적인 알고리즘

def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        temp = a[i]
        j = i - 1  #0부터 시작 j 초기화
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]  #삽입할 공간이 생기도록 j인덱스의 값을 오른쪽으로 한칸 이동
            j -= 1
        a[j+1] = temp #찾은 삽입 위치에 템프(key)를 저장

d = [4, 2, 5, 1, 3]
insert_sort(d)
print(d)

