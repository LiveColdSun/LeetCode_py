'''
# Solution version 1
# TLE when input:  "baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*"
class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        # len == 0
        if len(p) == 0:
            return len(s) == 0
        # len == 1
        if len(p) == 1:
            return (len(s) == 1) and (s[0] == p[0] or p[0] == '.')
        # len > 1 ,next char is '*'
        if p[1] != '*':
            if len(s) == 0:
                return False
            else:
                return (s[0] == p[0] or p[0] == '.') and (self.isMatch(s[1:],p[1:]))
        # next char is '*', more complicated
        while (len(s) > 0) and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s,p[2:])
'''


# Solution Version 2 with DP . AC succeed .
class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(p)+1):
            if p[i-1] == '*' and i >= 2:
                dp[0][i] = dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[len(s)][len(p)]
