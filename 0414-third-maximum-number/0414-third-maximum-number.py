class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        nums.sort(reverse=True)  # Sort in descending order
        if len(nums) >= 3:
            return nums[2]  # Return the third largest
        return nums[0]  # If fewer than 3 distinct numbers, return the largest
