from math import factorial
from functools import lru_cache
mod=1000003
f=[1]*(1000001)
mf=[1]*(1000001)
for i in range(1,1000001):
    f[i]=((i%mod)*f[i-1])%mod

for i in range(1,1000001):
    mf[i]=pow(f[i], mod-2,mod)

for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    an=(f[n]*((mf[k]%mod)*(mf[n-k]%mod)))%mod
    print(f"Case {t}: {an:.0f}")