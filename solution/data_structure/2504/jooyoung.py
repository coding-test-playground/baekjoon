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
        print("result:{}, answer:{}".format(result, answer))
        stack.append(word[i])
    elif word[i] == "[":
        result *= 3
        print("result:{}, answer:{}".format(result, answer))
        stack.append(word[i])
    elif word[i] == ")":
        if word[i - 1] == "(":
            answer += result
        if not stack or stack[-1] != "(":  # 올바른 괄호열이 아니라면
            answer = 0
            break
        result //= 2
        stack.pop()
        print("result:{}, answer:{}".format(result, answer))
    elif word[i] == "]":
        if word[i - 1] == "[":
            answer += result
        if not stack or stack[-1] != "[":  # 올바른 괄호열이 아니라면
            answer = 0
            break
        result //= 3
        stack.pop()
        print("result:{}, answer:{}".format(result, answer))
if len(stack) == 0:
    print(answer)
else:
    print(0)
'''
첫번째! 괄호를 리스트로 하나씩 받아온다!

두번째! 괄호의 종류에 따라 각 다른 케이스를 둔다. '(' ')' '[' ']' 이렇게 4가지가 될 것!

세번째! 케이스를 나눈다!
세번째-1 ! ( 나 [ 와 같이 열린 괄호가 들어올 경우?! 2나 3을 한 변수에 곱해주고 (변수 초기값은 1. 0이면 아무리 곱해도 0이니까~) 올바른 괄호 판단 알고리즘대로 stack에 append 해준다.
세번째-2 ! )나 ] 와 같이 닫힌 괄호가 들어올 경우?! 일단 stack이 비지는 않았는지, stack[-1]이 짝이 지어진 괄호가 맞는지 ('('의 짝은 ')', '['의 짝은 ']')를 먼저 체크한다. 여기서 틀리면 result=0 해주고 바로 break 🏳 ~! 맞으면 괄호가 닫혔으므로 2나 3을 다시 나눠주고, stack.pop() 해준다.

네번째! 닫힌괄호 앞의 괄호를 확인해보자!
세번째-2 전에 처리해줘야하는 과정이다. 만약에 닫힌 괄호가 들어왔고, 그 직전에 짝이 맞는 열린 괄호가 들어왔다면? 그 두 괄호는 쌍이 맞고 가장 안 쪽에 있으므로 애기 괄호가 된다. (예를 들면 () 또는 [] 순으로 들어왔을 때) 그럼 이 지점에서 result를 업데이트 해줘야 한다. 왜? 괄호의 한 케이스가 끝났으니까! 그니까 result += res 해줘버리자~

다섯번째! 결과를 출력하자!
위의 과정이 모든 과정이 끝났다. 그리고 이제 판단을 해보자. 일단 만약에, stack이 아직 비어있지 않다면..? 올바른 괄호가 아니라는 뜻! 0을 출력해주자.
stack도 잘 비어있으면? 올바른 괄호이므로 계산 결과를 출력해주자. result 출력하기!
'''
