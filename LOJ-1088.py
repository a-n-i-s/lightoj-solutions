import bisect
for t in range(1,int(input())+1):
    n,q=map(int,input().split())
    a=tuple(map(int,input().split()))
    print(f"Case {t}:")
    for _ in range(q):
        l,r=map(int,input().split())
        an=bisect.bisect_right(a, r)-bisect.bisect_left(a, l)
        print(an)
