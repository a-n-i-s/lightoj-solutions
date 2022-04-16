from functools import reduce
from math import gcd
for t in range(1,int(input())+1):
    n=int(input())
    a=map(int,input().split())
    an=reduce(lambda x,y:(x*y)//gcd(x,y),a)
    print(f"Case {t}: {an}")