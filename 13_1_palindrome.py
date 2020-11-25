# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력 : 문자열 s
# 출력 : 회문이면 True, 아니면 False

def palindroms(s):
    que_q = []
    stack_s = []

# 1단계 : 문자열의 알파벳 문자를 각각 큐와 스택에 넣음!
    for x in s:
        if x.isalpha(): #공백, 특수, 숫자는 isalpha()로 걸러냄!!
            que_q.append(x.lower())
            stack_s.append(x.lower())
    print(que_q)
# 2단계 : 큐와 스택에 들어 있는 문자르 꺼내면서 비교!

    while que_q:
        if que_q.pop(0) != stack_s.pop():  #pop(0) 맨앞, pop() 맨뒤
            return False
    return True

print(palindroms("Wow"))
print(palindroms("Madam, I'm Adam."))
print(palindroms("Madam, I am Adam.")) 

