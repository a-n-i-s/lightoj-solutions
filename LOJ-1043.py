from math import sqrt
def area(ab,bc,ca):
    s=(ab+bc+ca)/2
    return sqrt(s*(s-ab)*(s-bc)*(s-ca))

def ok(ab,bc,ca,r,ad):
    abc=area(ab, bc, ca)
    de=(ad/ab)*bc
    ea=(ad/ab)*ca
    ade=area(ad, de, ea)
    return r>(ade/(abc-ade))

for t in range(1,int(input())+1):
    ab,bc,ca,rat=map(float,input().split())
    l,r=0,ab
    for _ in range(100):
        m=(l+r)/2
        if ok(ab,bc,ca,rat,m):
            l=m
        else:
            r=m
    print(f"Case {t}: {l:.9f}")