for t in range(1,int(input())+1):
    n,p=input().split()
    n=int(n)
    if p[0]=='A':
        an='Bob' if (n%3)==1 else 'Alice'
    else:
        an='Bob' if n%3 else 'Alice'
    
    print(f'Case {t}: {an}')