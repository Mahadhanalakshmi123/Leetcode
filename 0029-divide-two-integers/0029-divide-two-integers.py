class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handling overflow for 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Edge case for overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values to simplify
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Subtract the divisor using bitwise shifting to speed up
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign of the result
        quotient = -quotient if negative else quotient
        
        # Ensure the result is within the 32-bit signed integer range
        return max(MIN_INT, min(MAX_INT, quotient))
