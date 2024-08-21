N, K = [int(i) for i in input().split()]

coins = [int(input()) for i in range(N)]

cnt = 0
for c in reversed(coins):
    if c > K: continue
    cnt += K // c
    K %= c
    if K==0: break

print(cnt)
