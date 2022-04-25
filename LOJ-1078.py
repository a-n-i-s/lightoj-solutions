for t in range(1,int(input())+1):
    n,d=map(int,input().split())
    an,m=0,0
    for _ in range(10**9):
        an+=1
        m=((m*10)+d)%n
        if m==0:
            break
    print(f"Case {t}: {an}")