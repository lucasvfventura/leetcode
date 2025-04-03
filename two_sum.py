class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        half = {}
        for i, num in enumerate(nums):
            half[target - num] = i

        for i, num in enumerate(nums):
            pair_index = half.get(num)
            if pair_index != None and pair_index != i :
                first = half[num]
                return [i, first]

        return []