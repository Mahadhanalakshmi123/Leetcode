class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        
        # XOR all characters in s and t
        for char in s + t:
            result ^= ord(char)
        
        # Convert result back to character
        return chr(result)
