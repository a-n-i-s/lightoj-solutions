from math import factorial
from functools import lru_cache

@lru_cache()
def f(n):
    return factorial(n)

for t in range(1,int(input())+1):
    n=int(input())
    an=[]
    for i in  range(19,-1,-1):
        if f(i)<=n:
            n-=f(i)
            an.insert(0, str(i))
            
    
    
    an="impossible" if n else '!+'.join(an)+'!'
    print(f"Case {t}: {an}")
    