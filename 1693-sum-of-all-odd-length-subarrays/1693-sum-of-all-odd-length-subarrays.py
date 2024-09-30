from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)

        # Iterate through all possible starting points for subarrays
        for start in range(n):
            # Iterate through all possible lengths of the subarrays
            for length in range(1, n - start + 1, 2):  # step by 2 for odd lengths
                total_sum += sum(arr[start:start + length])
        
        return total_sum

# Example usage
solution = Solution()
print(solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))  # Output: 58
print(solution.sumOddLengthSubarrays([1, 2]))           # Output: 3
print(solution.sumOddLengthSubarrays([10, 11, 12]))     # Output: 66
