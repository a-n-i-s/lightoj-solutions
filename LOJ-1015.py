for t in range(1,int(input())+1):
    input()
    n=input()
    an=sum(list(map(lambda x:0 if x[0]=='-' else int(x),input().split())))
    print("Case "+str(t)+":",an)