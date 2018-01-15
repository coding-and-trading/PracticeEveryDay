import unittest as ut

class TestSolutionMethods(ut.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        test_str1 = 'abcdabc'
        self.assertEqual(4, s.lengthOfLongestSubstring(test_str1))
        test_str2 = 'abc'
        self.assertEqual(3, s.lengthOfLongestSubstring(test_str2))
        test_str2 = 'a'
        self.assertEqual(1, s.lengthOfLongestSubstring(test_str2))

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        find all substrings and return length of longest
        """
        if s is '':
            raise ValueError("s shoun't be empty string.")

        all_substring = [self.getSubString(i, s) for i in range(len(s))]

        return len(max(all_substring, key=lambda x:len(x)))

    def getSubString(self, index, s):
        """
        return substring which index at 'index'
        :param index: 
        :param s: 
        :return: 
        """
        substring = s[index:len(s)]
        for i in range(len(substring)):
            if i is 0:
                continue
            if substring[0] == substring[i]:
                return substring[0:i]

        return s[index:len(s)]      # return all string if have no substring

if __name__ == '__main__':
     ut.main()