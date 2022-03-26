for t in range(1,int(input())+1):
    n,p,q=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    an,w=0,0
    for i in a[:p]:
        if w+i<=q:
            w+=i
            an+=1
    print(f"Case {t}: {an}")
    