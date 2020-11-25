
def print_all_friend(g, start):
    qu = []
    done = set()

    qu.append((start, 0)) 
    done.add(start)

    while(qu):
        (f_names, points) = qu.pop()
        print(f_names, points)
        for name in g[f_names]:
            if name not in done:
                qu.append((name, points + 1))
                done.add(name)

fr_info = {
    "Summer" : ["John", "Justin", "Mike"],
    "John" : ["Summer", "Justin"],
    "Justin" : ["John", "Summer", "Mike", "May"],
    "Mike" : ["Summer", "Justin"],
    "May" : ["Justin", "Kim"],
    "Kim" : ["May"],
    "Tom" : ["Jerry"],
    "Jerry" : ["Tom"]
}

print_all_friend(fr_info, "Summer")
print("====")
print_all_friend(fr_info, "Jerry")
print("====")
print_all_friend(fr_info, "Mike")