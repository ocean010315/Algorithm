import sys

S = set()
M = int(input())
for i in range(M):
    query = sys.stdin.readline().strip().split()

    if len(query)==1:
        if query[0]=="all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        n = int(query[1])
        if query[0]=='add':
            S.add(n)
        
        if query[0]=="remove":
            S.discard(n)
        
        if query[0]=="check":
            print(1) if n in S else print(0)
        
        if query[0]=='toggle':
            if n in S:
                S.discard(n)
            else:
                S.add(n)