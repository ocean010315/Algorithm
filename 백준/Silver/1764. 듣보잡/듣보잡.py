N, M = [int(i) for i in input().split()]

neverHeard = set([input() for n in range(N)])
neverSeen = set([input() for m in range(M)])

never = sorted(list(neverHeard & neverSeen))
print(len(neverHeard&neverSeen))
[print(name) for name in never]