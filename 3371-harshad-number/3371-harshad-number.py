class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        sum = 0
        while x > 0:
            rem = x % 10
            sum += rem
            x = x // 10
        if temp % sum == 0:
            return sum
        else:
            return -1
