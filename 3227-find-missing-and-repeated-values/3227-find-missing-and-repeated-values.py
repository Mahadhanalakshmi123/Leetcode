class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n
        freq = [0] * (n2 + 1)
        
        for row in grid:
            for num in row:
                freq[num] += 1
        
        repeating = missing = -1
        
        for i in range(1, n2 + 1):
            if freq[i] == 2:
                repeating = i
            elif freq[i] == 0:
                missing = i
        
        return [repeating, missing]
