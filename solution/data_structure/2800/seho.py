import sys

def input():
    return sys.stdin.readline().rstrip()

result = []
base_count = 0
ins = ''

def strip(s, count):
    lstack = []
    findcount = 0
    flag = False
    ret = ''
    for i in range(len(s)) :
        if flag == False:
            if s[i] == '(':
                findcount += 1
                if findcount >= count and len(lstack) == 0:
                    lstack.append(s[i])
                    continue
                if findcount >= count:
                    lstack.append(s[i])

            elif s[i] == ')':
                if findcount >= count:
                    lstack.pop()
                if findcount >= count and len(lstack) == 0:
                    flag = True
                    continue

        ret += s[i]

    return ret


def solution(s, count, skip_count):
    global base_count
    #base case
    if count == base_count:
        if s == ins:
            return
        if s not in result :
            result.append(s)
        return
    else :
        count += 1
    
    solution(s, count, skip_count)
    solution(strip(s, count-skip_count), count, skip_count+1)
    

def main():
    global base_count
    global ins
    ins = input()
    for i in ins:
        if i == '(':
            base_count += 1

    #print("base_count : ",base_count)

    solution(ins, 0, 0)

    result.sort()
    for i in result:
        print(i)

main()