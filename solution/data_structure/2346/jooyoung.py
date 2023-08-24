'''
2346
풍선 안에는 종이가 있다
제일 처음은 1번 풍선을 터뜨리고
풍선안에 있는 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적힌 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동
'''
N = int(input())
balloon = [i + 1 for i in range(N)]  # 풍선
number = list(map(int, input().split()))
result = ""
while True:
    result += str(balloon.pop(0)) + " "
    num = number.pop(0)  # 3

    if len(balloon) == 1:
        result += str(balloon.pop())
        break

    if num > 0:  # 양수라면
        for _ in range(num - 1):
            balloon.append(balloon.pop(0))
            number.append(number.pop(0))

    else:  # 음수라면 왼쪽 회전
        balloon.reverse()
        number.reverse()

        for i in range(len(number)):
            number[i] = -number[i]

        num = (-num)
        for _ in range(num - 1):
            balloon.append(balloon.pop(0))
            number.append(number.pop(0))

print(result)

'''
reverse 한 상태에서 오른쪽으로 회전하는 것 == 왼쪽으로 회전하는 것
종이 숫자들을 양수는 음수로 음수는 양수로 바꿔주면 된다.
'''
