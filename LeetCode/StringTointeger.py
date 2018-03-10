import re
import unittest as ut

class TestSolutionMethods(ut.TestCase):
    def test_myAtoi(self):
        s = Solution()
        s1 = '-123'
        s2 = '0'
        s3 = ''
        s4 = '-'

        self.assertEqual(-123, s.myAtoi(s1))
        self.assertEqual(0, s.myAtoi(s2))
        self.assertEqual(0, s.myAtoi(s3))
        self.assertEqual(0, s.myAtoi(s4))

class Solution:
    def myAtoi(self, str):
        """
        possible input like : '+-1', '+--3', ...
        :type str: str
        :rtype: int
        """
        if str is '-':
            return 0

        intPattern = re.compile("^[0-9-]+$")
        if re.match(intPattern, str) is None:
            return 0

        flag = None
        for x in str:
            value = x == ''
            if
        return int(str)

if __name__ == '__main__':
    ut.main()
