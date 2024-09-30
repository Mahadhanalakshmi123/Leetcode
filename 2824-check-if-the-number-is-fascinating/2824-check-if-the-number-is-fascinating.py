class Solution:
    def isFascinating(self, n: int) -> bool:
        # Calculate 2*n and 3*n
        two_n = 2 * n
        three_n = 3 * n
        
        # Concatenate n, 2*n, and 3*n as strings
        concatenated = str(n) + str(two_n) + str(three_n)
        
        # Check if the concatenated string contains all digits from 1 to 9 exactly once
        return len(concatenated) == 9 and set(concatenated) == set('123456789')

# Example usage
solution = Solution()
print(solution.isFascinating(192))  # Output: True
print(solution.isFascinating(100))  # Output: False
