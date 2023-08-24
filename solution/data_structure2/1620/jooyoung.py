'''
1620
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def sol1():
    stack = []
    answer = []

    for _ in range(N):
        stack.append(input())

    for _ in range(M):
        q = input()
        if q.isdigit():
            q = int(q) - 1
            answer.append(stack[q])
        elif q.isalpha():
            answer.append(stack.index(q) + 1)

    for i in answer:
        print(i)


def sol2():
    stack = {}

    for i in range(1, N + 1):
        stack[i] = input()

    reverse_stack = {v: k for k, v in stack.items()}

    for i in range(N):
        q = input()
        if q.isdigit():
            q = int(q)
            print(stack[q])
        else:
            print(reverse_stack[q])


def sol3():
    dic = {}

    for i in range(1, N + 1):
        a = input().rstrip()
        dic[i] = a
        dic[a] = i

    for i in range(M):
        question = input().rstrip()
        if question.isdigit():
            print(dic[int(question)])
        else:
            print(dic[question])


sol3()
