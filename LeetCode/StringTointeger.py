import re
import unittest as ut

class TestSolutionMethods(ut.TestCase):
    def test_myAtoi(self):
        s = Solution()
        s1 = '-123'
        s2 = '0'
        s3 = ''
        s4 = '-'
        s5 = '--+45'
        s6 = '+-89'
        s7 = '9'
        s8 = '    010'

        self.assertEqual(-123, s.myAtoi(s1))
        self.assertEqual(0, s.myAtoi(s2))
        self.assertEqual(0, s.myAtoi(s3))
        self.assertEqual(0, s.myAtoi(s4))
        self.assertEqual(0, s.myAtoi(s5))
        self.assertEqual(0, s.myAtoi(s6))
        self.assertEqual(9, s.myAtoi(s7))
        self.assertEqual(10, s.myAtoi(s8))

class Solution:
    def myAtoi(self, int_str):
        """
        possible input like : '+-1', '+--3', ...
        :type str: str
        :rtype: int
        """
        #if str is '-':
        #    return 0

        int_str = int_str.strip()
        int_pattern = re.compile("^[-+]?\d+$")
        if re.match(int_pattern, int_str) is None:
            return 0

        first_flag = None

        for x in range(0, len(int_str)):
            if int_str[x] is not '-' and int_str[x] is not '+':
                break
            value = 1 if int_str[x] is '+' else 0
            if first_flag is None:
                first_flag = value
                continue
            first_flag = 1 if first_flag is value else 0
        first_flag = 1 if first_flag is None else first_flag
        first_flag = '+' if first_flag is 1 else '-'

        int_str_without_flag = re.compile("\d+$")
        match = re.search(int_str_without_flag, int_str)
        final_str = first_flag + match.group()
        return int(final_str)

if __name__ == '__main__':
    ut.main()
#    s = Solution()
#    print(s.myAtoi('--+34'))
