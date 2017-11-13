class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            raise ValueError("nums must have two or greater elements.")
        result = []
        for frist_index, frist in enumerate(nums):
            print(frist_index)
            print(frist)
            for seconde_index,seconde in enumerate(nums[frist_index+1:]):
                if frist + seconde == target:
                    result.append([frist_index, seconde_index])
                    return result

        return []  # return empty list  if not found the solution

t = [3, 2, 4]
target = 6
s = Solution()
print(t[0:])
print(s.twoSum(t, target))