from math import sqrt,acos
def dis(x1,y1,x2,y2):
    return sqrt(((x1-x2)**2) + ((y1-y2)**2))

for t in range(1,int(input())+1):
    ox,oy,ax,ay,bx,by=map(int,input().split())
    r=dis(ax,ay,ox,oy)
    ab=dis(ax,ay,bx,by)
    an= acos((( 2*r*r) - ab**2)/(2*r*r) )*r
    print(f"Case {t}: {an}")
    