for t in range(1,int(input())+1):
    a=input()
    b='.'.join(list(map(lambda x:str(int(x,2)),input().split('.'))))
    an="Yes" if a==b else "No"
    print(f"Case {t}: {an}")
    