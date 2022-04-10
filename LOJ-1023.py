from itertools import permutations
for t in range(1,int(input())+1):
    print(f"Case {t}:")
    n,k=map(int,input().split())
    s=map(lambda x:chr(x+65), range(n))
    for i in permutations(s):
        if k==0:
            break
        k-=1
        print(''.join(i))