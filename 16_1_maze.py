# 조금더 공부 하자!!!!
maze ={
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b', 'd'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b', 'g', 'i'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j', 'o'],
    'l' : ['h', 'p'],
    'm' : ['i', 'n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}

def solve_maze(g, start, end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1] #큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야할 꼭지점
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p + ' -> ' + x)
                done.add(x)  #미로 종료점이 없을경우 대비
    
    return "?? 종료점이 없음"

print(solve_maze(maze, 'a', 'p'))
print(solve_maze(maze, 'a', 'z'))