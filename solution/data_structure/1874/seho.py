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