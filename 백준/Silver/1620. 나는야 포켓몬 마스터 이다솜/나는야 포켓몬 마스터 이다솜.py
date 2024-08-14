N, M = [int(i) for i in input().split()]

pokemon = {}
for n in range(N):
    name = input()
    pokemon[str(n+1)] = name
    pokemon[name] = str(n+1)

for m in range(M):
    print(pokemon[input()])