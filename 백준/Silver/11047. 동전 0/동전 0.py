N, K = [int(i) for i in input().split()]

coins = [int(input()) for i in range(N)]
coins.reverse()

cnt = 0
for c in coins:
    if c > K: continue
    cnt += K // c
    K %= c
    if K==0: break

print(cnt)