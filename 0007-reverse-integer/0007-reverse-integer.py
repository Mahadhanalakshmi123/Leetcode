class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Store the sign of the integer
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value of x
        reversed_x = int(str(abs(x))[::-1])
        
        # Reapply the sign to the reversed integer
        result = sign * reversed_x
        
        # Return 0 if the result is out of 32-bit integer bounds
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
