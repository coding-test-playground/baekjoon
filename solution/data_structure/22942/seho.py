import sys
def input():
    return sys.stdin.readline().rstrip()
def main():
    N = int(input())
    circle_list = []
    for i in range(N):
        c, r = map(int, input().split())
        circle_list.append((c-r, c+r))
    
    circle_list.sort() 

    #print(circle_list)

    s = []
    s.append(circle_list[0])

    for i in range(1, N):
        l_bound, r_bound = circle_list[i]
        j = len(s) - 1
        
        while(j >= 0): # stack에 있는 원과 겹치는 케이스 모두 체크
            l_check, r_check = s[j]

            #print("새로운 넣을 원 :", l_bound, r_bound)
            #print("스택안의 기존 원 : ", l_check, r_check)
           
            if (l_check <= l_bound) and (l_bound <= r_check) and (r_check <= r_bound) : 
                print('NO')
                return
            elif r_check == l_bound: 
                print('NO')
                return
            if r_check > l_bound : # 새로 스택에 넣을 원이 스택 안의 모든 원의 오른쪽 바깥에 있는 경우를 찾기 위함
                s.clear()
                break
            j -= 1


        s.append((l_bound, r_bound))
        


    print('YES')
                

main()