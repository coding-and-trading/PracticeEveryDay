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
            distance = frist_index + 1
            for seconde_index,seconde in enumerate(nums[distance:]):
                if frist + seconde == target:
                    return [frist_index, seconde_index + distance]

        return []  # return empty list  if not found the solution
