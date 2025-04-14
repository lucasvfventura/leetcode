class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appearances = {}
        size = len(nums)/2
        for n in nums:
            count = appearances.get(n, 0) +1
            if count > size:
                return n
            appearances[n] = count
        
        return 0