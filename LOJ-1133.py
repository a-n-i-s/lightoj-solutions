from math import floor,ceil
for t in range(1,int(input())+1):
    n,q=map(int,input().strip().split())
    a=list(map(int,input().split()))
    for _ in range(q):
        qt,_,qb=input().partition(' ')
        if qt=='S':
            d=int(qb)
            for i in range(n):
                a[i]=a[i]+d
        if qt=='M':
            d=int(qb)
            for i in range(n):
                a[i]=a[i]*d
        if qt=='D':
            d=int(qb)
            for i in range(n):
                a[i]=a[i]/d
                a[i]=ceil(a[i]) if a[i]<0 else floor(a[i]) 
        if qt=='P':
            x,y=map(int,qb.split())
            a[x],a[y]=a[y],a[x]
        if qt=='R':
            d=[]
            for i in range(n):
                d.append(a[i])
            for i in range(n):
                a[i]=d[n-i-1]

        

            
    an=' '.join(str(i) for i in a)
    print(f"Case {t}:\n{an}")
    