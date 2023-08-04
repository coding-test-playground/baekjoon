import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    curr_iron = 0
    result = 0
    s = []

    iron_razor = deque(input())
    
    #for i in range(1, len(iron_razor) - 1): # 처음은 항상 (,  끝은 항상 )
    #    if iron_razor[i] == '(' and iron_razor[i-1] == '(':
    #        curr_iron += 1 # i-1이 쇠막대기

    s.append(iron_razor.popleft())
    for i in range(1, len(iron_razor)):
        pop_elem = iron_razor.popleft()
        if pop_elem == '(':
            if s[-1] == '(': # 이전 (는 쇠막대기 : curr 증가, result +1
                curr_iron += 1
                result += 1
                s.append(pop_elem)
            
            else: #else : #s[-1] == ')' # 알 수 없음 - 다음 스텝을 확인해봐야함
                s.append(pop_elem)
        else: 
            if s[-1] == '(': # 레이저인 경우 curr만큼 result 증가
                result += curr_iron
            else: # 쇠막대기의 오른쪽 끝인경우 : curr 감소, result 영향 x
                curr_iron -= 1
            s.append(pop_elem)
            
    print(result)


main()