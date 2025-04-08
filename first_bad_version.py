# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while right - left > 1:
            mid_point = (right - left + 1)//2 + left
            if isBadVersion(mid_point):
                right = mid_point
            else:
                left = mid_point
        
        return right