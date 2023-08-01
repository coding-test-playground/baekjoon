'''
1966
문서의 중요도
문서들 중 현재 문서보다 중요도가 높은 문서가 있담녀 queue 의 가장 뒤에 배치
'''
Testcase = int(input())
result = ""
for testcase in range(Testcase):
    cnt = 0
    N, M = map(int, input().split())  # 문서 개수, 몇번째로 인쇄 되었는지 궁금한 문서가 몇번째 위치해 있는지
    q = list(map(int, input().split()))
    idx = list(range(len(q)))  # 인덱스 배열

    # 내가 찾고 싶은 문서
    idx[M] = 'M'

    while True:
        if q[0] == max(q):  # 첫번째 문서가 가장 큰 중요도일때
            cnt += 1  # 출력 횟수를 늘려준다
            if idx[0] == 'M':  # 그리고 그 첫번째가 궁금한 문서일 경우
                result += str(cnt) + "\n"
                break
            else:
                q.pop(0)
                idx.pop(0)
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))

print(result)
