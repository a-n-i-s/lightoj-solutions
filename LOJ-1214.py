for t in range(1,int(input())+1):
    a,b=map(int,input().split())
    an='not divisible' if a%b else 'divisible'
    print(f"Case {t}: {an}")
    