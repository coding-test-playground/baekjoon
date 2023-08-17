'''
2493
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다
'''


def sol2():
    N = int(input())
    top = list(map(int, input().split()))  # 입력 받은 탑

    stack = []  # 탑을 넣을 스택
    result = [0] * N

    for i in range(len(top)):
        while stack:
            if stack[-1][1] < top[i]:  # 현재 탑보다 왼쪽 탑이 작을 경우 스택에서 제거한다 -> 어차피 레이저 수신 못하기 때문
                stack.pop()
            else:
                result[i] = stack[-1][0] + 1  # 만약에 왼쪽의 탑이 더 크다면 왼쪽 탑 번호를 현재 위치에 저장해준다
                break
        stack.append((i, top[i]))  # 탑의 인덱스랑 탑의 길이를 같이 저장해줌 i , i-1 형태로 저장해야하기 때문에
    print(" ".join(map(str, result)))


def sol1():
    N = int(input())
    top = list(map(int, input().split()))  # 입력 받은 탑

    pop_top = list(top)  # 탑을 복사
    c = 0  # 검사용이자 탑의 번호를 임시 저장
    result = []
    for i in range(len(top)):
        a = pop_top.pop()  # stack 의 가장 뒤에 있는 요소 4
        j = -1
        c = 0
        for _ in range(len(pop_top)):  # 마지막 요소가 제거되어 남은 탑 중에서
            b = pop_top[j]
            if b >= a:  # 뒤에서부터 4보다 크거나 같은 요소를 찾는다
                # 만약 4보다 크거너 같다면 그 요소를 저장하고 반복문을 break
                c = top.index(b) + 1
                break
            else:  # 만약 4보다 작다면 그 요소는 건너뛴다
                j -= 1

        # 반복문 후 에 c 에 값이 없다면
        if c:
            result.append(c)
        else:
            result.append(0)

    result.reverse()
    print(" ".join(map(str, result)))


sol1()
sol2()
