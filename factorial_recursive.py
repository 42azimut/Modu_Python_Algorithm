def recur_fact(num):
    if num < 1:
        return 1
    return num * recur_fact(num -1)

print(recur_fact(5))
print(recur_fact(10))

#4-1 연습문제 페이지 59p
def recur_sum(num2):
    if num2 < 0:
        return 0
    return num2 + recur_sum(num2 - 1)
print(recur_sum(50))

#4-2 연습문제 페이지 59p
def recur_max_num(max_list, len_list):
    if len_list == 1:
        return max_list[0]
    max_num = recur_max_num(max_list, len_list-1)   
    if max_num > max_list[len_list -1]:
        return max_num
    else: 
        return max_list[len_list-1]

list_find = [17, 22, 334, 23, 1, 9, 4, 10, 56]
print(recur_max_num(list_find, len(list_find)))
