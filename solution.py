Here is a Python console application that implements a wildcard pattern matcher with support for `?` and `*`.

```python
def match(input, pattern):
    length = len(input)
    if len(pattern) - pattern.count('*') > length:
        return False

    dp = [[False] * (length + 1) for _ in range(len(pattern) + 1)]
    dp[0][0] = True

    for i in range(1, len(pattern) + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
            for j in range(1, length + 1):
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        elif pattern[i - 1] == '?' or pattern[i - 1] == input[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = False

    return dp[-1][-1]

def main():
    input = input("Enter the input string: ")
    pattern = input("Enter the pattern: ")
    if match(input, pattern):
        print("Match found!")
    else:
        print("Match not found!")

if __name__ == "__main__":
    main()
```

This program uses dynamic programming to solve the problem. The `match` function creates a 2D boolean array `dp` where `dp[i][j]` is `True` if the first `i` characters in `pattern` match the first `j` characters in `input`. It then iterates over `pattern` and `input` and updates `dp` according to the rules of the wildcard pattern matching. Finally, it returns the last element in `dp`, which indicates whether `pattern` matches `input`.

The `main` function gets the `input` and `pattern` from the user, calls `match` with these values, and prints whether a match was found.