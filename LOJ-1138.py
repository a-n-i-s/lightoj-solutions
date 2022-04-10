from math import factorial
from functools import lru_cache

@lru_cache()
def get_zeroes(n):
    d,r=5,0
    while d<=n:
        r+=n//d
        d*=5
    return r

@lru_cache()
def minimum_greater_equal(x,l=-1,r=1000000000,fun=lambda x:x):
    while l+1<r:
        m=(l+r)//2
        if fun(m)>=x:
            r=m
        else:
            l=m
    return r

for t in range(1,int(input())+1):
    n=int(input())
    an=minimum_greater_equal(n,fun=get_zeroes)
    if get_zeroes(an)!=n:
        an='impossible'
    print(f"Case {t}: {an}")
    