import sys
sys.set_int_max_str_digits(10000)  # Increase the limit, e.g., to 10,000 digits

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_1 = int(num1)
        num_2 = int(num2)
        return str(num_1 + num_2)
