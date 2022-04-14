for t in range(1,int(input())+1):
    n=int(input())
    a=list(map(int,input().split()))
    d=dict(map(lambda x:(x[1],x[0]),enumerate(a)))
    an=0
    for i in range(n):
        if a[i]!=i+1:
            p=d[i+1]
            a[i],a[p]=a[p],a[i]
            d[a[i]]=i
            d[a[p]]=p
            an+=1

    print(f"Case {t}: {an}")
