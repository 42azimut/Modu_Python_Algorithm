# 최대값의 위치(인덱스 값)을 구하시오!

list = [17, 22, 334, 23, 1, 9, 4, 10, 56]

def find_max_index(max_list):
    len_list = len(max_list)
    max_idx = 0
    for i in range(1, len_list):
        if max_list[i] > max_list[max_idx]:
            max_idx = i 
    return max_idx  

print(find_max_index(list))
print(list[find_max_index(list)])