from math import acos,sin
for t in range(1,int(input())+1):
    r1,r2,r3=map(float,input().split())
    ab=r1+r3
    bc=r3+r2
    ca=r2+r1
    abc=acos((ab**2+bc**2-ca**2)/(2*ab*bc))
    bac=acos((ab**2+ca**2-bc**2)/(2*ab*ca))
    bca=acos((bc**2+ca**2-ab**2)/(2*bc*ca))
    an=(.5*bc*ab*sin(abc))-.5*((abc*r3*r3)+(bca*r2*r2)+(bac*r1*r1))
    print(f"Case {t}: {an:.9f}")
    