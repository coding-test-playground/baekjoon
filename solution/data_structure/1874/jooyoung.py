'''
1874

'''
n = int(input())
sequence = []  # 원하는 수열
stack = []  # 내가 쌓을 수열
cnt = 1
flag = True
answer = []
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        flag = False
        break


if flag:
    for i in answer:
        print(i)

