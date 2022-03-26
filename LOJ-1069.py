for t in range(1,int(input())+1):
    a,b=map(int,input().split())
    an=(abs(a-b)+a)*4+19
    print(f"Case {t}: {an}")