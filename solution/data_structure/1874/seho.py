'''
풀이 요약

각 줄에서 입력되는 숫자 k가
    다음에 stack에 넣을 수 보다 큰 경우에는 stack을 k로 채워넣고 k를 증가시킨다.
    만약 입력된느 숫자가 k보다 작은 경우에는 stack에서 해당 숫자가 나올때까지 빼고
        해당 숫자가 나오면 빼는 것을 멈춘다.
        만약 stack에서 뺀 숫자가 입력된 숫자보다 작은경우는 해당 수열을 만들 수 없으므로 NO를 출력한다.    
'''

import sys

s = []
result = []


def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    k = 1 # stack에 넣을 수
    
    for i in range(n):
        target_num = int(input())
        
        while(True):
            if target_num >= k :
                s.append(k)
                result.append("+")
                k += 1
            elif target_num < k:
                #print(s)
                pop_num = s.pop()
                result.append("-")
                
                if pop_num == target_num:
                    break
                elif pop_num > target_num:
                    print("NO")
                    return
                
    for i in result:
        print(i)
        

main()