
d=[0]*1001
for i in range(1001):
    for j in range(1,i+1):
        if i%j==0:
            d[i]+=1

an=list(sorted(range(1001),key=lambda x:(d[x],-x)))
for t in range(1,int(input())+1):
    n=int(input())
    print(f"Case {t}: {an[n]}")
    