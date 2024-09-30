class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Find the minimum of a and b
        min_ab = min(a, b)
        count = 0
        
        # Check each number from 1 to min_ab
        for i in range(1, min_ab + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        
        return count

# Example usage
solution = Solution()
print(solution.commonFactors(12, 6))  # Output: 4
print(solution.commonFactors(25, 30)) # Output: 2
