for t in range(1,int(input())+1):
    input()
    n,k=map(int,input().split())
    d=set()
    for _ in range(n):
        d.add(int(input().split()[1]))
    d=sorted(d)

    an,l,s=1,0,0
    for j in range(len(d)):
        s=d[j]-d[l]
        if s>k:
            an+=1
            l=j
        
    print(f"Case {t}: {an}")
