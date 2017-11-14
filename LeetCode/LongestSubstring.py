class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        find all substrings and return length of longest
        """
        substrings = []

        for index, word in enumerate(s):
            