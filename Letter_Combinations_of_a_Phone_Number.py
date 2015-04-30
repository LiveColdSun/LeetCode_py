class Solution:
    # @param {string} digits
    # @return {string[]}

    def letterCombinations(self, digits):
        dic = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
               '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        result = []
        for i in digits:
            if result == []:
                for item in dic[i]:
                    result.append(item)
            else:
                tmpresult = []
                for tmp in result:
                    for item in dic[i]:
                        tmpresult.append(tmp+item)
                result = tmpresult
        return result
