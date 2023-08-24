import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    a = set()
    count = 0
    
    for i in range(n):
        s = input()
        a.add(s)

    for i in range(m):
        test = input()
        if test in a:
            count+=1
    
    print(count)
    
    

main()