from math import log,ceil
from itertools import accumulate

d=list(accumulate(range(1000001),lambda x,y:x+log(y,10)))

for t in range(1,int(input())+1):
    n,b=map(int,input().split())
    an=max(1,d[n]/log(b,10))
    print(f"Case {t}: {ceil(an)}")