#최대값 구하기!

list = [17, 22, 334, 23, 1, 9, 4, 10, 56]

def find_max(n):
    len_n = len(n)
    max_value = n[0]
    for i in range(1, len_n):
        if max_value < n[i]:
            max_value = n[i]
    return max_value

print(find_max(list))