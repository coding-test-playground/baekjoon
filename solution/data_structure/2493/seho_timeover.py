# 시간초과
def main():
    n = int(input())
    towers = list(map(int, input().split()))

    toin = []    
    answer = []

    for i in range(n):
        toin.append((towers[i], i+1))
        
    toin.sort(key=lambda x : x[0], reverse=True) 

    maxin = 0
    for i in range(n):
        ans = 0

        for j in range(i):
            if toin[j][1] < toin[i][1] and ans < toin[j][1]:
                ans = toin[j][1]
        
        answer.append((toin[i][1], ans))
    
    for i in sorted(answer):
        print(i[1], end=' ')
    
    
main()