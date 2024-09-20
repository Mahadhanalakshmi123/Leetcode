class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ''.join([c.lower() for c in s if c.isalnum()])
        return filtered_str == filtered_str[::-1]

        