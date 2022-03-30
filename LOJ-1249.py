
def f(x):
    return (int(x[1])*int(x[2])*int(x[3]),x[0])
for t in range(1,int(input())+1):
    a=sorted([f(input().split()) for _ in range(int(input()))])
    an="no thief" if a[0][0]==a[-1][0] else f"{a[-1][1]} took chocolate from {a[0][1]}"
    print(f"Case {t}: {an}")
    