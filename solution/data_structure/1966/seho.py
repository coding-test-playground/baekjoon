
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    prQueue = deque()
    first_max = -1
    first_max_index = -1
    
    for i in range(n): # n개 테스트 케이스
        count = 0
        docNum, targetIndex = map(int, input().split())
        prQueue = deque(map(int, input().split()))
        first_max_index = 0

        while(True):
            first_max = prQueue[0]
            first_max_index = 0
            #print("first max"+str(first_max))
            for j in range(len(prQueue)): # first max 찾기
                if prQueue[j] > first_max : # 같은 수가 나와도 첫번째만 찾음
                    first_max = prQueue[j]
                    first_max_index = j
            
            if (first_max_index == targetIndex):
                print(count + 1)
                break
            #else
            
            for j in range(first_max_index): # first max가 가장 앞으로 올 때까지 회전
                temp = prQueue.popleft()
                prQueue.append(temp)
            
            prQueue.popleft() # first max 출력(큐에서 제외)
            
            count = count + 1 # 현재까지 출력된 문서 개수

            
            if first_max_index < targetIndex: # 이동된 target Index 계산
                targetIndex -= (first_max_index+1)
            else :
                targetIndex = len(prQueue) + (targetIndex - first_max_index)

            #print(prQueue, first_max_index, targetIndex)


main()