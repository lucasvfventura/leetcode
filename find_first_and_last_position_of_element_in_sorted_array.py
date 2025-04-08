class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def pivot_index(left, right):
            return (right - left + 1)//2 + left
        
        if len(nums) == 0:
            return [-1, -1]

        l = 0

        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            pivot = pivot_index(left_index, right_index)
            if nums[pivot] < target and (pivot == (len(nums) - 1) or nums[pivot +1] > target):
                return [-1, -1]

            if nums[pivot] == target and (pivot == 0 or nums[pivot -1] < target):
                l = pivot
                break

            if nums[pivot] >= target:
                right_index = pivot -1
            else:
                left_index = pivot +1

        if right_index < 0 or left_index > len(nums) - 1:
            return [-1, -1]

        r = 0
        left_index = l
        right_index = len(nums) - 1
        while left_index <= right_index:
            pivot = pivot_index(left_index, right_index)

            if nums[pivot] == target and (pivot == len(nums) - 1 or nums[pivot +1] > target):
                r = pivot
                break

            if nums[pivot] > target:
                right_index = pivot -1
            else:
                left_index = pivot +1 
        
        return [l, r]