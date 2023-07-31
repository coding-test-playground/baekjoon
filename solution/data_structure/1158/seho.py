import sys

def input():
    return sys.stdin.readline().rstrip()


n, k = map(int,input().split())
ysps = [i+1 for i in range(n)]

curr = 0
result = '<'
while(True):
    curr = (curr + k - 1) % (len(ysps))
    
    result = result + str(ysps.pop(curr))
    if(len(ysps) == 0) :
        result = result + '>'
        break
    result = result + ', '

print(result)