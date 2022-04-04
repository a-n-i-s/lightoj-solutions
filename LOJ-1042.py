def next_perm(s):
    n=len(s)
    l,r=-1,-1
    for i in range(n-2,-1,-1):
        if s[i]<s[i+1]:
            l=i
            break
    for i in range(n-1,l,-1):
        if s[l]<s[i]:
            r=i
            break
    s=s[:l]+s[r]+s[l+1:r]+s[l]+s[r+1:]
    return int(s[:l+1]+s[:l:-1],2)


for t in range(1,int(input())+1):
    n=int(input())
    an=next_perm('0'+bin(n)[2:])

    print(f"Case {t}: {an}")