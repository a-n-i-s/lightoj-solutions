for t in range(1,int(input())+1):
    a=list(map(int,input().split()))  #a,b,c,d,e,f=a[0 to 5]; n=a[6]
    for i in range(a[6]):
        a[:5],a[5]=a[1:6],sum(a[:6])
    print("Case "+str(t)+": "+str(a[0]%10000007))