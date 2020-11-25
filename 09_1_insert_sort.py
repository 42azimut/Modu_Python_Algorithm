# 리스트 r, v가 들어가야할 위치(인덱스) 리턴 함수
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

#print(find_ins_idx(d, 5))

def insert_sort(a):
    result = []
    while a:  #리스트a 에 남아 있는동안 루프!
        value = a.pop(0)  #리스트에서 맨 앞을 뽑아!
        insert_idx = find_ins_idx(result, value) #위 함수에서 값의 들어갈 인덱스를 찾음
        result.insert(insert_idx, value) #그 인덱스에 그 값을 리스트에 삽입!\
        print(a, result)
    return result
d = [2, 3, 5, 1, 4, 8, 6, 12]
print(insert_sort(d))