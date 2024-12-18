class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current element with the sum of itself and the minimum of the two adjacent numbers below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # The top element now contains the minimum path sum
        return triangle[0][0]
