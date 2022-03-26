for t in range(1,int(input())+1):
    n=input()
    a=list(map(int,input().split()))
    d={}
    for i in a:
        d[abs(i)]=i
    an=sum(d.values())
    print(f"Case {t}: {an}")
    