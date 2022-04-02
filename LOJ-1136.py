for t in range(1,int(input())+1):
    a,b=map(int ,input().split())
    an=b - ((b-1)//3+1)  - ((a-1 - ((a-2)//3+1)) if a>1 else 0)
    print(f"Case {t}: {an}")
