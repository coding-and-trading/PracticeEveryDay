import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        intPattern = re.compile("^[0-9-]+$")
        if re.match(intPattern, str) is False:
            raise ValueError("Invalid input")

