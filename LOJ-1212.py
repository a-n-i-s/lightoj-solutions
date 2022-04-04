from collections import deque
for t in range(1,int(input())+1):
    print(f"Case {t}:")
    q=deque()
    n,l=map(int,input().split())
    for _ in range(l):
        c=input().split()
        if c[0]=='pushLeft':
            if len(q)<n:
                q.appendleft(c[1])
                print(f"Pushed in left: {c[1]}")
            else:
                print("The queue is full")

                
        
        if c[0]=='pushRight':
            if len(q)<n:
                q.append(c[1])
                print(f"Pushed in right: {c[1]}")
            else:
                print("The queue is full")


        if c[0]=='popLeft':
            if len(q)>0:
                print(f"Popped from left: {q.popleft()}")
            else:
                print("The queue is empty")

        if c[0]=='popRight':
            if len(q)>0:
                print(f"Popped from right: {q.pop()}")
            else:
                print("The queue is empty")

                
                