# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력 : 모든 친구의 이름!

def print_all_friends(g, start):
    qu = []  # 기억장소 1: 앞으로 처리해야할 사람들을 큐에 저장
    done = set() # 기억장소 2 : 이미 큐에 추가한 사람들을 집합에 기록(set중복 방지)

    qu.append(start) #자신을 큐 리스트에 넣고 시작
    done.add(start) #집합에도 자신을 넣고 시작

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)  # 리스트에 추가(중복 가능)
                done.add(x)  #set() 추가.. 중복 방지!

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

print_all_friends(fr_info, "Summer")
print("====")
print_all_friends(fr_info, "Jerry")
print("====")
print_all_friends(fr_info, "Mike")