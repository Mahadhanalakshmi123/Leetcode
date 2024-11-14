from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        # Custom comparator function to decide the order of numbers
        def compare(x, y):
            # Compare concatenated strings x + y vs y + x
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # They are equal
        
        # Convert all numbers to strings
        nums_str = list(map(str, nums))
        
        # Sort the numbers using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # If the largest number is 0, return "0"
        if nums_str[0] == "0":
            return "0"
        
        # Join the sorted list into a single string and return it
        return ''.join(nums_str)
