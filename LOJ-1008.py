import math
for t in range(int(input())):
    n=int(input())
    x=math.floor(math.sqrt((n-1)))
    r,c=x+1,n-(x)**2
    if c>r:
        c=r-c%r
        r,c=c,r

    if x%2:
        r,c=c,r
    print("Case "+str(t+1)+":",r,c)