for t in range(1,int(input())+1):
    an='odd' if bin(int(input())).count('1')%2 else 'even'
    print(f"Case {t}: {an}")
    