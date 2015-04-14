class Solution:
    # @return an integer
    def reverse(self, x):
        neg = -1 if x < 0 else 1
        x = 0-x if x < 0 else x
        result = 0
        while x > 0:
            result = result*10 + (x % 10)
            x /= 10
        if result > 2**31:
            return 0
        return result*neg

