from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Check triplets to find a valid triangle
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                # Valid triangle found
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        # No valid triangle found
        return 0

# Example usage
solution = Solution()
print(solution.largestPerimeter([2, 1, 2]))      # Output: 5
print(solution.largestPerimeter([1, 2, 1, 10]))  # Output: 0
