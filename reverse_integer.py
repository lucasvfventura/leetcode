class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        v = int(str(abs(x))[::-1])
        if v > 2**31:
            return 0
        
        return -v if is_negative else v
        

