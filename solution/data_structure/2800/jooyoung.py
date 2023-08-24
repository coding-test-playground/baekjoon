'''
2800
sort 로 내림차순 정렬해주면 된다

'''


def dfs(depth=0, combi=[]):
    if depth == len(couple):
        do_test(combi)
        return
    for i in range(2):  # 0,1
        combi.append(i)
        dfs(depth + 1, combi)
        combi.pop(-1)


def do_test(combi):
    a = list(word)
    if 0 not in combi:
        return
    for i in range(len(combi)):
        if combi[i] == 0:  # 괄호 제거
            a[couple[i][0]] = None
            a[couple[i][1]] = None

    a = ''.join([c for c in a if c is not None])  # none 값 제거하고 문자열로 변환
    if a not in answer:
        answer.append(a)


word = list(input())
stack = []
couple = []
answer = []

# 괄호쌍의 인덱스 저장
for i in range(len(word)):
    if word[i] == '(':
        stack.append(['(', i])
    elif word[i] == ')':
        couple.append([stack[-1][-1], i])
        stack.pop()

dfs()
answer.sort()

for i in range(len(answer)):
    print(answer[i])
