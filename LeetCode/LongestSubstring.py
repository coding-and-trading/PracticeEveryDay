class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        find all substrings and return length of longest
        """
        if s is '':
            raise ValueError("s shoun't be empty string.")

        substrings = []

        for index, word in enumerate(s):
            find_it = False
            for end, element in enumerate(s[index+1:]):
#                print(s[index+1:])
                if element in s[index:end+1]:
#                    print('element is %s' %(element))
#                    print('word is %s' %(s[index:end+1]))
                    substrings.append(s[index:end+1])
                    find_it = True
                    break
            if not find_it:
                substrings.append(s[index:])
        print(substrings)
        return max([len(x) for x in substrings])

s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = ''
solution = Solution()
print(solution.lengthOfLongestSubstring(s4))