import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    total = 0
    tmap = {}
    while(True):
        tr = input()
        if tr == '':
            break
        else :
            if tr in tmap:
                tmap[tr] += 1
                total +=1
            else :
                tmap[tr] = 1
                total +=1
        
    tlist = sorted(tmap)

    for i in tlist:
        print('%s %.4f' % (i, tmap[i]/ total * 100))


main()

