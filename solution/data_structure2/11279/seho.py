import sys
import math

import heapq

def input():
    return sys.stdin.readline().rstrip()

'''
def main():
    N = int(input())
    maxheap = []
    for i in range(N):
        cmd = int(input())
        if cmd == 0:
            if (len(maxheap) == 0):
                print(0)
                continue
            maxvalue = max(maxheap)
            print(maxvalue)
            maxindex = maxheap.index(maxvalue)
            maxheap.pop(maxindex)
        else :
            maxheap.append(cmd)
'''

# max heap 구현 - 시간초과
class maxheap():
    def __init__(self):
        self.val = []
        self.nodenum = 0

    def add(self, cmd): # 새로들어온 노드를 마지막에 추가하고, 부모노드와 비교하면서 추가
        self.val.append(cmd)
        self.nodenum += 1
        cur = self.nodenum - 1
        for j in range(int(math.log2(self.nodenum))):
            parent = int((cur - 1) / 2)
            if self.val[parent] < self.val[cur] :
                temp = self.val[parent]
                self.val[parent] = self.val[cur]
                self.val[cur] = temp
                continue
            else:
                break
        

    def popmax(self):
        if len(self.val) == 0:
            print(0)
            return

        print(self.val[0])
        # 가장 앞(최대값) 노드 제거 후 마지막 원소를 처음으로
        self.val[0] = self.val[self.nodenum-1]
        self.val = self.val[:self.nodenum-1]
        self.nodenum -= 1

        if self.nodenum == 0 :
            return
        
        # 처음으로 옮긴 노드를 자식노드와 비교하면서 원위치
        cur = 0 # 비교하면서 옮겨가는 위치
        for j in range(int(math.log2(self.nodenum))):
            lchild = int(cur*2 +1) if cur*2 +1 <= self.nodenum-1 else -1
            rchild = int(cur*2 +2) if cur*2 +2 <= self.nodenum-1 else -1

            greaterchild = max([lchild, rchild])
            #if greaterchild == -1 : # 자식이 없음
            #    continue

            if self.val[greaterchild] > self.val[cur]:
                temp = self.val[cur]
                self.val[cur] = self.val[greaterchild]
                self.val[greaterchild] = temp
                cur = greaterchild
                continue
            else :
                break



def main():
    N = int(input())
    maxh = maxheap()

    for i in range(N):
        cmd = int(input())
        if cmd == 0:
            maxh.popmax()
                    
        else : 
            maxh.add(cmd)
            
           


'''
def main():
    heap = []
    N = int(input())
    
    for i in range(N):
        cmd = int(input())
        if cmd == 0:
            if len(heap) == 0:
                print(0)
                continue
            print(-heapq.heappop(heap))
                    
        else : 
            heapq.heappush(heap, -cmd)
'''

main()