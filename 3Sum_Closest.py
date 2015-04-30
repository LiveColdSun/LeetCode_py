class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        i, nums = 0, sorted(nums)
        dis = abs(nums[0] + nums[1] + nums[2] - target)
        result = nums[0] + nums[1] + nums[2]
        while i < len(nums)-2:
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                elif nums[i] + nums[j] + nums[k] < target:
                    if target - (nums[i] + nums[j] + nums[k]) < dis:
                        dis = target - (nums[i] + nums[j] + nums[k])
                        result = nums[i] + nums[j] + nums[k]
                    j += 1
                else:
                    if nums[i] + nums[j] + nums[k] - target < dis:
                        dis = nums[i] + nums[j] + nums[k] - target
                        result = nums[i] + nums[j] + nums[k]
                    k -= 1
            i += 1

        return result
