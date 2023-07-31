import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    for i in range(n):
        ps = input()
        
        p_open = 0
        result = 'YES'

        if ps[0] == ')': # 첫번째 괄호가 ) 인 경우
            result = 'NO'
            

        for j in ps:
            if p_open < 0 : # 열리지 않았는데 닫힌 경우
                result = 'NO'
                break
            elif j == '(':
                p_open = p_open + 1
            else :
                p_open = p_open - 1
            
        if p_open == 0:
            result="YES"
            print(result)
        else :
            result='NO'
            print(result)



if __name__ == "__main__":
    main()