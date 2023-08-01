import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
       
    n_map = {}
    j=0
    temp_map = {}

    for i in range(n):
        temp = input()
        n_map[str(chr(ord('A') + i))] = temp
       

    while(True):
        for i in range(len(s)):
            if s[i] == '*': 
                temp = float(n_map[s[i-2]]) * float(n_map[s[i-1]])
                n_map[str(chr(ord('a') + j))] = temp

                if i < len(s) - 1: # 마지막이 아닌경우
                    s = s[:i-2] + str(chr(ord('a') + j)) + s[i+1:]
                else :
                    s = s[:i-2] + str(chr(ord('a') + j))
                #print(s)
                j=j+1
                break
                

            elif s[i] == '+':
                temp = float(n_map[s[i-2]]) + float(n_map[s[i-1]])
                n_map[str(chr(ord('a') + j))] = temp

                if i < len(s) - 1: 
                    s = s[:i-2] + str(chr(ord('a') + j)) + s[i+1:]
                else :
                    s = s[:i-2] + str(chr(ord('a') + j))
                #print(s)
                j=j+1
                break

            elif s[i] == '-':
                temp = float(n_map[s[i-2]]) - float(n_map[s[i-1]])
                n_map[str(chr(ord('a') + j))] = temp

                if i < len(s) - 1: 
                    s = s[:i-2] + str(chr(ord('a') + j)) + s[i+1:]
                else :
                    s = s[:i-2] + str(chr(ord('a') + j))
                #print(s)
                j=j+1
                break

            elif s[i] == '/':
                temp = float(n_map[s[i-2]]) / float(n_map[s[i-1]])
                n_map[str(chr(ord('a') + j))] = temp

                if i < len(s) - 1: 
                    s = s[:i-2] + str(chr(ord('a') + j)) + s[i+1:]
                else :
                    s = s[:i-2] + str(chr(ord('a') + j))
                #print(s)
                j=j+1
                break


        if len(s) == 1:
            print(format(float(n_map[s]),".2f"))
            
            break

main()