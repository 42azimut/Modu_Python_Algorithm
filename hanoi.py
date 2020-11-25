# 원반 개수 n
# 옮길 원반이 현재 있는 출발점 기둥 from_pos
# 원반을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조기중 aux_pos
# 출력 : 원반을 옮기는 순서! 

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        return print(from_pos, "->", to_pos)

    
    # 원반 n-1개를 aux_pos로 이동(to_pos를 보조기둥으로 이용)
    hanoi(n-1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)

    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로 이용)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n ======= 1")
hanoi(1, 1, 3, 2)

print("n ======== 2")
hanoi(2, 1, 3, 2)

print("n ========= 3")
hanoi(7, 1, 3, 2)


#n_ = 2**64

def year_hanoi(n_):
    sec = n_
    min = sec / 60
    hour = min / 60
    day = hour / 24
    year = day / 365
    yymmdd = input(year)
    yy = int(yymmdd[:4])
    mm = int(yymmdd[4:6])
    return yy, mm
print(year_hanoi(2**64))
print(2**64)

print(yy, mm)

