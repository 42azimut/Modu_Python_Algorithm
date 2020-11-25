# 리스트에서 특정 숫자 모두 찾기

def search_list_all(a, x):
    n = len(a)
    list_num = []
    for i in range(0, n):
        if (x == a[i]):
            list_num.append(i)
    if list_num == []:
        list_num.append(-1)
    return list_num

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list_all(v, 18))
print(search_list_all(v, 33))
print(search_list_all(v, 142))
