from math import asin
def ok(a,b):
    r=(((a**2)+(b**2))**.5)/2
    return ((4*(asin(b/(2*r)))*r)+(2*a))<400


for t in range(1,int(input())+1):
    a,b=map(int,input().split(':'))
    l,r=0,400
    for _ in range(100):
        m=(l+r)/2
        if ok(m,m*b/a):
            l=m
        else:
            r=m
    print(f"Case {t}: {l:.9f} {l*b/a:.9f}")
