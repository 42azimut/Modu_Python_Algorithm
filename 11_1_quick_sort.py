def qucik_sort(a):
    n = len(a)
    if n <= 1:
        return a
    
    pivot = a[-1]
    g1 = [] 
    g2 = []
    for i in range(0, n-1):  #마지막 원소는 pivot에 들어가서 범위에서 뺸다!
        if a[i] < pivot:
            g1.append(a[i])
            #print(g1)
        else:
            g2.append(a[i])
            #print(g2)
    return qucik_sort(g1) + [pivot] + qucik_sort(g2)  

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
q_list = qucik_sort(d)
print(q_list)
