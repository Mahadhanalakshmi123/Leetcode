class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Handle optional sign
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        # Step 3: Convert the string to integer by reading digits
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
        
        # Step 4: Apply sign and handle overflow
        result *= sign
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
