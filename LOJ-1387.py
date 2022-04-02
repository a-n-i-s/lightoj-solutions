for t in range(1,int(input())+1):
    print(f"Case {t}:")
    s=0
    for _ in range(int(input())):
        c=input()
        if c.startswith('r'):

            print(s)
        else:
            s+=int(c.split()[1])