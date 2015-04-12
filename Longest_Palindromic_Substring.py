# -*- coding: utf-8 -*-
'''
 Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
 and there exists one unique longest palindromic substring.
'''

'''
暴力方法：固定头元素，从字符串末尾查找相同元素，并确定之间元素是否为回文子串。
时间复杂度O(N^3),空间复杂度O(1)
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        longest = 0  # to store the length of the longest Palindrome
        longstr = ''
        i = 0
        while i < len(s) and len(s)-i > longest:
            j = len(s)-1  # from the last character
            while j > i:
                if s[j] == s[i] and longest < j-i+1:
                    l = i
                    r = j
                    while l < r and s[l] == s[r]:
                        l += 1
                        r -= 1
                    if not l < r:
                        longest = j-i+1
                        longstr = s[i:j+1]
                        break
                j -= 1
            i += 1
        return longstr
'''


# 中心查找法：时间复杂度O(N^2),空间复杂度O(1)
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        longest, longstr = 0, ''
        i, j = (len(s) - 1)/2, len(s)/2
        while i >= 0 and j < len(s):
            args = [(s,i,i), (s, i, i+1), (s, j, j), (s,j,j+1)]
            for arg in args:
                stemp = self.PalindromewithCenter(*arg)
                if len(stemp) > longest:
                    longest, longstr = len(stemp), stemp
            if longest >= i*2:
                break
            i, j = i-1, j+1
        return longstr

    def PalindromewithCenter(self, s, l, r):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
