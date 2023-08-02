import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input()) # 풍선 개수, 적힌 숫자 범위
    balloon = [i+1 for i in range(n)]
    paper = list(map(int, input().split()))
    
    curr_index = 0
    result = []

    while(True):
        result.append(balloon.pop(curr_index)) # 터뜨린 풍선의 번호
        paper_temp = paper.pop(curr_index)
        
        #print("current index : ", curr_index)
        print(str(result[-1])+" ", end='')

        if len(balloon) == 1:
            result.append(balloon.pop(0))
            print(result[-1], end='')
            break

        if paper_temp > 0:
            curr_index = (curr_index + paper_temp) % len(balloon) - 1
            if curr_index < 0:
                curr_index = curr_index + len(balloon)
        else:
            if (curr_index + paper_temp) >= 0:
                curr_index = curr_index + paper_temp
            else:
                if -(curr_index + paper_temp) % len(balloon) != 0:
                    tempint = int(-(curr_index + paper_temp) / len(balloon)) + 1
                else:
                    tempint = int(-(curr_index + paper_temp) / len(balloon))
                curr_index = (curr_index + paper_temp) + len(balloon) * tempint
            



main()