class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digit in str(num):
            val = int(digit)
            if num % val == 0:
                count += 1
        return count
