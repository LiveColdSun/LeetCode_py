class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman_dic = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        i, result = 0, 0
        while i < len(s):
            if i < len(s)-1:
                if not roman_dic[s[i]] < roman_dic[s[i+1]]:
                    result += roman_dic[s[i]]
                    i += 1
                else:
                    key = s[i] + s[i+1]
                    result += roman_dic[key]
                    i += 2
            else:
                result += roman_dic[s[i]]
                i += 1
        return result
