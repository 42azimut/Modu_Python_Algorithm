# 두번 이상 나온 이름 찾기 리스트에서..
# 입력 : 이름이 n개 있는 리스트
# 출력 : 이름이 n개중 반복되는 이름의 집합!

def samename(list_a):
    length = len(list_a)
    result = set()
    for i in range(0, length - 1):
        for j in range (i+1, length):
            if list_a[i] == list_a[j]:
                result.add(list_a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name))


