N = int(input())  # 피연산자 개수
stack = []
asc = 65

postfix = [i for i in input()]

num = dict()

for i in range(N):
    num[chr(asc)] = input()
    asc += 1

for i in postfix:
    # 영문자라면 숫자로 변환 필요
    if 'A' <= i <= 'Z':
        stack.append(int(num[i]))
    else:  # 연산자라면
        one = stack.pop()
        two = stack.pop()
        if i == "*":
            stack.append(two * one)
        elif i == "/":
            stack.append(two / one)
        elif i == "+":
            stack.append(two + one)
        elif i == "-":
            stack.append(two - one)


print("{:.2f}".format(stack[0]))

'''
처음에는 리스트에 모두 쌓아놓은 다음 계산하는 방식을 생각했고 
다음에는 하나씩 쌓으면서 연산자가 쌓이게 되면 숫자를 stack 에서 꺼내서 계산하면 되겠다고 생각했다. 
연산을 하고 나서의 숫자를 어떻게 할지 몰라 고민을 했는데 구글링 해보니 연산한 값은 어차피 다시 사용될 것이기 
때문에 다시 stack 에 넣어주면 재활용된다 !
'''