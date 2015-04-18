class Solution:
    # @param height, an integer[]
    # @return an integer
    def maxArea(self, height):
        i, j, largest = 0, len(height)-1, 0
        while i < j:
            largest = max(largest, (j-i)*min(height[i], height[j]))
            # move the index with lower value
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return largest
