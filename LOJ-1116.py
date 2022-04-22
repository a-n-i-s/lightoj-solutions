
for t in range(1,int(input())+1):
    n=int(input())
    c=0
    while n and n%2==0:
        c+=1
        n//=2
    an= "Impossible" if c==0 else ' '.join(map(str,(n,2**c)))
    
    print(f"Case {t}: {an}")