from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        length = 0
        odd_found = False
        
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
                
        # Add 1 if there's at least one character with an odd frequency
        if odd_found:
            length += 1
            
        return length
