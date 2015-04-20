class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        num_dic = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        num_key, result = sorted(num_dic.keys(), reverse=True), ''
        for i in range(len(num_key)):
            while num >= num_key[i]:
                result += num_dic[num_key[i]]
                num -= num_key[i]
        return result
