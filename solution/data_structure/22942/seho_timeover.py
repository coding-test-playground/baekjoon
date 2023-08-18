import sys
def input():
    return sys.stdin.readline().rstrip()
def main():
    N = int(input())
    circle_list = []
    for i in range(N):
        c_curr, r_curr = map(int, input().split())
        l_bound = c_curr - r_curr
        r_bound = c_curr + r_curr

        for j in circle_list: # j[0] : 왼쪽 경계, j[1] : 오른쪽 경계
            if j[0] > l_bound and j[0] < r_bound and j[1] > r_bound: # 왼
                print('NO')
                return
            elif j[1] > l_bound and j[1] < r_bound and l_bound > j[0]: # 오
                print('NO')
                return
            elif j[0] == l_bound or j[0] == r_bound or j[1] == l_bound or j[1] == r_bound: # 접하는 경우
                print('NO')
                return
        

        circle_list.append((l_bound, r_bound))
    

    print('YES')
                

main()