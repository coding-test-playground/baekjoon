'''
10799
( 이 나오면 스택에 추가 () 이 나오면 ( 의 개수를 세고 +
) 이 나오면 1를 더해주고 스택에 있는 ( pop
'''

pipe = list(input())
stack = []
cnt = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')
    else:  # ) 일때
        if pipe[i - 1] == '(':  # '()' 라면
            stack.pop()
            cnt += len(stack)

        else:  # 레이저의 끝 부분인 ( 라면
            cnt += 1
            stack.pop()
print(cnt)
