class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        max_volume = 0
        while left < right:
            volume = min(height[left], height[right])*(right-left)
            if volume > max_volume:
                max_volume = volume
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        
        return max_volume
