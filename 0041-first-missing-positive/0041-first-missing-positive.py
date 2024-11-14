class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Move each number to its correct position (if possible)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers are in their correct position, return n + 1
        return n + 1
