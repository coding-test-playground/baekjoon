'''
22942

만나지 않는 경우
1. 두 원의 반지름 합 < 두 원의 중심 좌표 차
2. 두 원의 반지름의 차 > 두 원의 중심 좌표 차
3. 두 원의 중심 좌표 차 == 0

시간초과
'''
N = int(input())
circle = []  # 원의 정보를 저장
flag = True

# 스택에 저장하고 하나씩 꺼내가며 비교하는 방법
for _ in range(N):
    a, b = map(int, input().split())
    circle.append((a, b))
circle.sort()

while circle:
    x, r = circle.pop()
    for c in circle:
        x_ = c[0]
        r_ = c[1]
        if r + r_ < abs(x - x_):
            continue
        elif abs(r - r_) > abs(x - x_):
            continue
        elif abs(x - x_) == 0:
            continue
        else:  # 교점이 존재한다면
            flag = False
            break

    if not flag:
        break

if flag:
    print("YES")
else:
    print("NO")
