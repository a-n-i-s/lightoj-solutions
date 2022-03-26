for t in range(1,int(input())+1):
    x1,y1,x2,y2=map(int,input().split())
    print(f"Case {t}:")
    for _ in range(int(input())):
        x,y=map(int,input().split())
        print("Yes" if (x>x1 and x<x2 and y>y1 and y<y2) else "No")
    