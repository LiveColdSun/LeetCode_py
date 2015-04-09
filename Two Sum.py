class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        store = {}
        for i , n in enumerate(num):
            if target - n in store:
                return (store[target - n]+1, i+1)
            store[n] = i