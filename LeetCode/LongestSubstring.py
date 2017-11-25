class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        find all substrings and return length of longest
        """
        if s is '':
            raise ValueError("s shoun't be empty string.")

        substrings = {}

        for index, word in enumerate(s):
            print(index, word)
            next_index = index + 1
            # handle the last one
            if index == len(s)-1:
                break
            for end, element in enumerate(s[next_index:]):
                print(s[index:next_index+end])
                if element in s[index:next_index+end]:
                    # handle the last one
                    word = None
                    if next_index+end+1 == len(s)-1:
                        word = s[index:next_index+end+1]
                    else:
                        word = s[index:next_index+end]
                    substrings[word] = substrings.get(word, 0) + 1
                    break


        if len(substrings) == 0:
            substrings[s] = substrings.get(s, 0) + 1
        print(substrings)
        return max([len(k) for k, v in substrings.items()])

    def lengthOfLongestSubstring2(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwke'
s4 = 'aab'
solution = Solution()
print(solution.lengthOfLongestSubstring2(s4))