class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        div = 1
        while x/div >= 10:
            div *= 10
        while x != 0:
            left = x / div
            right = x % 10
            if left == right:
                x = (x % div) / 10
                div /= 100
            else:
                return False
        return True
