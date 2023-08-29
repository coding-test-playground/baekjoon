import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    h = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in line:
            if len(h) >= N:
                if h[0] > j:
                    continue
                else :
                    heapq.heappop(h)
                    heapq.heappush(h, j)
                    #print(h)
            else :
                heapq.heappush(h, j)
                #print(h)
                
    
    print(h[0])
        

main()