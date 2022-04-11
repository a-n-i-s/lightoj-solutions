for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    c=[int(input()) for _ in range(n+1)]

    def ok(x):
        s,m=0,0
        for i in c:
            if i>x:
                return 0
            if s+i>x:
                s=0
                m+=1
            if m>k:
                return 0
            s+=i
        return m<=k
    
    def solve():
        l,r=0,sum(c)
        while l+1<r:
            m=(l+r)//2
            if ok(m):
                r=m
            else:
                l=m
        print(f"Case {t}: {r}")
        s,id=0,0
        for i in range(k+1):
            if n-id>=k-i:
                while id<=n and s+c[id]<=r and n-id>=k-i:
                    s+=c[id]
                    id+=1
                print(s)
                s=0
            else:
                print(c[id])
                id+=1

    solve()
