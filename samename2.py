# page 47 연습문제 3-1

def samename2(name):

    len_name = len(name)
    
    for i in range(0, len_name -1):
        for j in range(i+1, len_name):
            print(name[i], "-", name[j])
        
    
name = ["Tom", "Jerry", "Mike", "Jone", "Shua"]
print(samename2(name))

num = range(10)
print(samename2(num))
