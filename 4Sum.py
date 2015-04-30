class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}

    def fourSum(self, nums, target):
        i, nums, result = 0, sorted(nums), []
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k, l = j + 1, len(nums) - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    else:
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        k, l = k + 1, l - 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                j += 1
                while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 1 and nums[i] == nums[i - 1]:
                i += 1
        return result
