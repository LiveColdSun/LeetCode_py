class Solution:
    # @param str, a string
    # @return an integer
    def myAtoi(self, s):
        if len(s) == 0:
            return 0
        sign, re, i, INT_MAX, INT_MIN = 1, 0, 0, 2147483647, -2147483648
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        while i < len(s) and '0' <= s[i] <= '9':
            re = re * 10 + ord(s[i]) - ord('0')
            i += 1
        re *= sign
        if re > INT_MAX:
            return INT_MAX
        if re < INT_MIN:
            return INT_MIN
        return re
