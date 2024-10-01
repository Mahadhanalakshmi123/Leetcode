class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total_sum += i
        return total_sum

# Example usage
solution = Solution()
print(solution.sumOfMultiples(7))  # Output: 21
print(solution.sumOfMultiples(10)) # Output: 40
print(solution.sumOfMultiples(9))  # Output: 30