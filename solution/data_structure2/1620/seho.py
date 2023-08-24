import re
import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, q = map(int,input().split())

    recheck = re.compile('[0-9]')

    poketmons = {}
    poketmons_num = {}
    result = []

    for i in range(N):
        num = i + 1
        name = input()
        poketmons[num] = name
        poketmons_num[name] = str(num)
    
    for i in range(q):
        qq = input()
        if recheck.match(qq) : # 숫자이면 (key)
        #if qq.isdigit():  # 시간초과
            result.append(poketmons[int(qq)])
        else : # 이름(value)이 주어진 경우
            result.append(poketmons_num[qq])
    
    for i in result:
        print(i)

main()