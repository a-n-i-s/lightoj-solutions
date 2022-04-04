from math import sqrt
for t in range(1,int(input())+1):
    ax,ay,bx,by,cx,cy=map(int,input().split())
    
    ba=((ax-bx),(ay-by))
    bc=((cx-bx),(cy-by))

    dx,dy = ba[0]+bc[0]+bx,ba[1]+bc[1]+by   #   ba + bc - b 

    area=abs((ba[0]*bc[1])-(ba[1]*bc[0]))   #   |ba x bc|


    print(f"Case {t}: {dx} {dy} {area}")
    