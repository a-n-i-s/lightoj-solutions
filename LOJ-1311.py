for t in range(1,int(input())+1):
    v1,v2,v3,a1,a2=map(float,input().split())
    t1=v1/a1
    d1=v1*t1-(a1*t1*t1)/2
    t2=v2/a2
    d2=v2*t2-(a2*t2*t2)/2
    d=d1+d2
    db=max(t1,t2)*v3
    
    print(f"Case {t}: {d:.9f} {db:.9f}")
    