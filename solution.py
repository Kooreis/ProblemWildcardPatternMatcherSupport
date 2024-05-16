def match(input, pattern):
    length = len(input)
    if len(pattern) - pattern.count('*') > length:
        return False

    dp = [[False] * (length + 1) for _ in range(len(pattern) + 1)]
    dp[0][0] = True