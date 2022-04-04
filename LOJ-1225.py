for t in range(1,int(input())+1):
    s=input()
    an="Yes" if s[::]==s[::-1] else "No"
    print(f"Case {t}: {an}")
    