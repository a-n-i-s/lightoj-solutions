for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    a=tuple(map(int,input().split()))

    def ok(x):
        c,s=0,0
        for i in a:
            if s+i>x:
                s=0
                c+=1
            if c>k:
                return False
            s+=i
        return c<k


    l,r=0,sum(a)
    while l+1<r:
        m=(l+r)//2
        if ok(m):
            r=m
        else:
            l=m
    an=max(max(a),r)
    print(f"Case {t}: {an}")
