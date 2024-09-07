T = int(input())
for t in range(T):
    n = int(input())
    
    clothes = {}
    for _ in range(n):
        a, b = input().split()

        if b in clothes:
            clothes[b].append(a)
        else:
            clothes[b] = [a]
    
    cnt = 1
    for i in clothes:
        cnt *= (len(clothes[i]) + 1)
    
    print(cnt-1)