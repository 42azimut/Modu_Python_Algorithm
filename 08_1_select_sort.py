print("===============select sorting 1st=========")

def sel_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print("id:", i, a)

d = [2, 3, 5, 1, 4, 8, 6, 12]
sel_sort(d)
print("sorted_result :", d)

print("===============select sorting 2nd=========")

def find_min_idx(a):
    n = len(a)
    min_idx2 = 0
    for i in range(1, n):
        if a[i] < a[min_idx2]:
            min_idx2 = i
    return min_idx2

def sel_sort(a):
    result = []
    while a:
        min_idx2 = find_min_idx(a)
        value = a.pop(min_idx2)
        result.append(value)
    return result

list_d = [2, 3, 5, 1, 4]
print(sel_sort(list_d))
