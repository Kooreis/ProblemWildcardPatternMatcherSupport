for i in range(1, len(pattern) + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
            for j in range(1, length + 1):
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]