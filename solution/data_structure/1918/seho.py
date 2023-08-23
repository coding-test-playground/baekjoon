import sys
def input():
    return sys.stdin.readline().rstrip()

def solution(s):
    st = []
    first_depth = True
    no_paran = True
    next = ''
    next_list = []
    oxlist = ['x' for x in range(len(s))]

    for i in range(len(s)): # 1뎁스 괄호 단위 찾아서 리스트로 저장
        if s[i] == '(' :
            if not first_depth :
                next = next + s[i]
            if len(st) == 0:
                first_depth = False
                no_paran = False
            st.append(s[i])
        elif s[i] == ')':
            st.pop()
            if len(st) == 0 : #
                first_depth = True
                next_list.append(next)
                next = ''
            if not first_depth :
                next = next + s[i]
        else :
            if s[i] != '*' and s[i] != '/' and s[i] != '+' and s[i] != '-' :
                oxlist[i] = 'o'
            if not first_depth :
                next = next + s[i]

    #print("target", s)
    #print("oxlist : ", oxlist)
    #print("next_list : ", next_list)

    # 괄호 모두 해체 후 */, +- 순으로 후위표기식으로 변환


    # 1뎁스 리스트 원소에 대해 모두 재귀 호출하고 결과값을 현재 결과값에 반영
    
    for i in next_list:
        temp_result = solution(i)
        start, end = (-1,-1)
        for j in range(len(s)):
            if s[j] == '(':
                if len(st) == 0:
                    start = j
                st.append(s[j])
            if s[j] == ')':
                st.pop()
                if len(st) == 0:
                    end = j
                    break
        
        if start != -1 and end != -1:
           s = s[:start] + temp_result + s[end+1:]
           oxlist = oxlist[:start] + ['o' for x in range(len(temp_result))] + oxlist[end+1:]

        # 위에서 temp_result 부분은 변환 완료된 부분으로 표기
    
    # base case , */, +- 순으로 후위표기식으로 변환하여 리턴
    for i in range(len(s)):
        pre, post = '', ''
        if (s[i] == '*' or s[i] =='/') and oxlist[i] == 'x':
            # find pre, post
            pre = i-1
            post = i+1
            
            while(True):
                if pre <= 0:
                    break
                elif oxlist[pre] == 'x':
                    pre += 1
                    break
                else :
                    pre -= 1
        
            while(True):
                if post >= len(s) - 1 :
                    break
                elif oxlist[post] == 'x':
                    post -= 1
                    break
                else :
                    post += 1

            #print(pre)
            #print(post)
            #print(s[:pre])
            #print(s[pre:i])
            #print(s[i+1:post+1])
            #print(s[i])
            #print(s[post+1:])

            s = s[:pre] + s[pre:i] + s[i+1:post+1] + s[i] + s[post+1:]
            oxlist[i] = 'o'
            #print(s)
            #print(oxlist) 

    #print("* / result : ", s)
            

    for i in range(len(s)):
        pre, post = '', ''
        if (s[i] == '+' or s[i] =='-') and oxlist[i] == 'x':
            # find pre, post
            pre = i-1
            post = i+1
            
            while(True):
                if pre <= 0:
                    break
                elif oxlist[pre] == 'x':
                    break
                else :
                    pre -= 1
        
            while(True):
                if post >= len(s) - 1 :
                    break
                elif oxlist[post] == 'x':
                    post -= 1
                    break
                else :
                    post += 1

            #print(pre)
            #print(post)
            #print(s[:pre-1])
            #print(s[pre:i])
            #print(s[i+1:post+1])
            #print(s[i])
            #print(s[post+1:])

            s = s[:pre] + s[pre:i] + s[i+1:post+1] + s[i] + s[post+1:]
            oxlist[i] = 'o' 

            #print(s)
            #print(oxlist) 

    #print("+ - result : ", s)

    return s
    



def main():
    s = input()
    result = ''
    
    result = solution(s)

    print(result)
    

main()