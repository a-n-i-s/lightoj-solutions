for t in range(1,int(input())+1):
    n=input()
    a=map(int,input().split())
    an,p=0,2
    for i in a:
        an+=(i-p)//5 +((i-p)%5!=0)
        p=i
    print(f"Case {t}: {an}")
    