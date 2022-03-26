for t in range(1,int(input())+1):
    a=sorted(input().lower().replace(' ', ''))
    b=sorted(input().lower().replace(' ', ''))
    an="Yes" if a==b else "No"
    print(f"Case {t}: {an}")
    