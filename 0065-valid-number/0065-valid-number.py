class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        
        # Regular expression for a valid number
        pattern = re.compile(r"""
            ^                  # Start of the string
            [+-]?              # Optional sign
            (                  # Start main group
                (\d+\.\d*)     # Digits followed by a dot and optional more digits
                |              # OR
                (\.\d+)        # A dot followed by digits
                |              # OR
                \d+            # Just digits
            )                  # End main group
            ([eE][+-]?\d+)?    # Optional exponent with 'e' or 'E' and optional sign
            $                  # End of the string
        """, re.VERBOSE)
        
        return bool(pattern.match(s))
