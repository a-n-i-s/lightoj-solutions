import math
for t in range(1,int(input())+1):
    r,c=map(int,input().split())
    if r>c:
        r,c=c,r
    if r==1:
        an=c
    elif r==2:
        an=(c//4)*4
        if c%4==3:
            an+=4
        else:
            an+=(c%4)*2
    else:
        an=(r*c)//2+(r*c)%2
    
    print("Case "+str(t)+":",an)