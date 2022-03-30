import calendar as c
from datetime import datetime

for t in range(1,int(input())+1):

    d1,y1=input().split(',')
    d2,y2=input().split(',')
    y1,y2=int(y1),int(y2)
    d1,d2=datetime.strptime(d1+' 2000', '%B %d %Y'),datetime.strptime(d2+' 2000', '%B %d %Y')
    
    an=c.leapdays(y1,y2+1)
    
    if c.isleap(y1) and d1>=datetime(d1.year,3,1):
        an-=1
    if c.isleap(y2) and d2<=datetime(d2.year,2,28):
        an-=1
    

    print(f"Case {t}: {an}")
    