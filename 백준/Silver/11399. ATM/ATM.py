N = int(input())

time = [int(i) for i in input().split()]
total = 0
for i, t in enumerate(sorted(time, reverse=True)):
    total += t * (i+1)
print(total)