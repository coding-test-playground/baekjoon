import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

flag = 1

def solution(s):
    lstack = []
    test = [] # [[])
    temps = ''
    local_result = 0
    global flag

    if s[0] == ')' or s[0] == ']':  # 정합성 체크
        flag = -1
        return
    
    temps = temps + s[0]
    test.append(s[0])
    opennum = 1

    for i in range(1, len(s)):
        if s[i] == '(' or s[i] == '[':
            temps = temps + s[i]
            test.append(s[i])
            opennum += 1

        elif s[i] == ')' or s[i] == ']':
            temps = temps + s[i]
            opennum -= 1
            if len(test) == 0:
                flag = -1
                return
            if s[i] ==  ')' :
                if test.pop() == '[':
                    flag = -1
                    return
            else :
                if test.pop() == '(':
                    flag = -1
                    return

            if opennum == 0 :
                lstack.append(temps)
                temps=''
    
    if opennum != 0: # 정합성 체크
        flag = -1
        return
    
    
    for param in lstack:
        if param == '()' :
            local_result += 2
        elif param == '[]' :
            local_result += 3
        elif param[0] == '(':
            local_result += 2*solution(param[1:-1])
        elif param[0] == '[' :
            local_result += 3*solution(param[1:-1])
    
    return local_result
      

def main():
    s = input()
    
    result = solution(s)
    
    if flag == 1:
        print(result)
    else:
        print(0)
    
    
main()