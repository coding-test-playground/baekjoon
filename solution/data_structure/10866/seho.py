import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    n = input()
    n = int(n)

    deque = []

    for i in range(n):
        cmd = input()
        if cmd.startswith("push_front") :
            number = cmd.split()[1]
            number = int(number)
            deque = [number] + deque
            #print(deque)
        elif cmd.startswith("push_back") :
            number = cmd.split()[1]
            number = int(number)
            deque.append(number)
            #print(deque)
        elif cmd == "pop_front":
            if(len(deque)==0):
                print(-1) 
            else:
                print(deque[0])
                deque = deque[1:]
        elif cmd == "pop_back":
            if(len(deque)==0):
                print(-1)
            else:
                print(deque[-1])
                #deque = deque[:-2]
                deque = deque[:-1]
        elif cmd == "size" :
            print(len(deque))
        elif cmd == "empty" :
            if len(deque) == 0 :
                print(1)
            else :
                print(0)
        elif cmd == "front" :
            if len(deque) == 0 :
                print(-1)
            else:
                print(deque[0])
        elif cmd == "back":
            if len(deque) == 0 :
                print(-1)
            else:
                print(deque[-1])
            
        
main()