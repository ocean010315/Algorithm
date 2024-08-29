T = int(input())

for _ in range(T):
    N = int(input())

    zeros, ones = 0, 0

    if N==0:
        zeros, ones = [1, 0]
    elif N==1:
        zeros, ones = [0, 1]
    elif N==2:
        zeros, ones =  [1, 1]
    else:
        dp = [[0, 0] for _ in range(N+1)]
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        dp[2] = [1, 1]
        for n in range(3, N+1):
            dp[n] = [dp[n-1][0] + dp[n-2][0], dp[n-1][1] + dp[n-2][1]]
        zeros, ones = dp[N]
    
    print(zeros, ones)