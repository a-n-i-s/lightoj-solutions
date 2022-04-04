for t in range(1,int(input())+1):
    a=sorted(list(map(int,input().split())))
    an="yes" if a[0]**2+a[1]**2==a[2]**2 else "no"
    print(f"Case {t}: {an}")