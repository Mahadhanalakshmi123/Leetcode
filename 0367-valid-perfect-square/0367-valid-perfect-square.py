class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num > 0:
            for i in range(1, num + 1):  # Start from 1 to num
                if num == i * i:
                    return True
                if i * i > num:  # Stop early if i*i exceeds num
                    break
        return False
