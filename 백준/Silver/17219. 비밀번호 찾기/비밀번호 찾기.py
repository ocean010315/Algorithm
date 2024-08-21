N, M = [int(i) for i in input().split()]

target = {}
for n in range(N):
    t, pw = input().split()
    target[t] = pw

for m in range(M):
    print(target[input()])