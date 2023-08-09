'''
2054 구글링 참고 풀이
'''
word = list(input())
answer = 0
result = 1
stack = []
for i in range(len(word)):
    if word[i] == "(":
        result *= 2
        # print("result:{}, answer:{}".format(result, answer))
        stack.append(word[i])
    elif word[i] == "[":
        result *= 3
        # print("result:{}, answer:{}".format(result, answer))
        stack.append(word[i])
    elif word[i] == ")":
        if word[i - 1] == "(":
            answer += result
        if not stack or stack[-1] != "(":  # 올바른 괄호열이 아니라면
            answer = 0
            break
        result //= 2 # () 이게 아니고, 올바른 괄호열이라면 그냥 나누기 2
        stack.pop()
        # print("result:{}, answer:{}".format(result, answer))
    elif word[i] == "]":
        if word[i - 1] == "[":
            answer += result
        if not stack or stack[-1] != "[":  # 올바른 괄호열이 아니라면
            answer = 0
            break
        result //= 3
        stack.pop()
        # print("result:{}, answer:{}".format(result, answer))
if len(stack) == 0:
    print(answer)
else:
    print(0)
'''
(()[[]])([])
2*(2+3*3)+(2*3)
2*2 + 2*3*3 + 2*3
괄호는 총 네가지로 분류된다.
첫번째 "(" 라면 -> 곱하기 2
두번째 "[" 라면 -> 곱하기 3
세번째 ")" 일때 전 단계에서 "("라면 계산이 완료된 것 . 즉 "()" 는 계산의 한 부분이 완료된 것이라고 볼 수 있다. 
그러므로 answer 를 갱신하고 곱하기 2했던 부분은 결국 필요가 없기 때문에 나누기 2를 해준다.
여기서 괄호가 쌍이 맞지 않거나 stack 이 비어있다면 answer = 0으로 고정되고 더 이상 계산이 필요하지 않게 된다.
네번째 "]" 일때 전 단계에서 "]"라면 계산이 완료된 것 . 즉 "[]" 는 계산의 한 부분이 완료된 것이라고 볼 수 있다.
'''
