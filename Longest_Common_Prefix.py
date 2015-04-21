class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        result = ''
        for i in range(min(len(strs[0]), len(strs[1]))):
            if strs[0][i] == strs[1][i]:
                result += strs[0][i]
            else:
                break
        for i in range(2, len(strs)):
            j = 0
            while j < min(len(result), len(strs[i])):
                if result[j] != strs[i][j]:
                    result = result[0:j]
                    break
                j += 1
            result = result[0:j]
        return result
