for t in range(1,int(input())+1):
    a,b,x,y=map(int,input().split())
    if abs(x-a)%2!=abs(y-b)%2:
        an="impossible"
    elif abs(x-a)==abs(y-b):
        an=1
    else:
        an=2
    print(f"Case {t}: {an}")
    