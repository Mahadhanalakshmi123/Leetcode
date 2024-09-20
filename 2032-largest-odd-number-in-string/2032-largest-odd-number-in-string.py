class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Start checking from the last digit towards the first
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  # If the digit is odd
                return num[:i+1]  # Return the substring up to and including this odd digit
        return ""  # Return empty string if no odd digit is found
