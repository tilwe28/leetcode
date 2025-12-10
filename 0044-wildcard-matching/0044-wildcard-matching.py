class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(p)][len(s)]


"""
- goal is to match every single character in s
- without '?' and '*', simply just match each character
- with '?', just skip over the character

- for '*' can't just skip until the next character is found
2d dp
row as p and column as s

  _ p a p e r
_ T F F F F F
* T T T T T T
p F T F T F F
? F F T F T F
r F F F F F T
"""