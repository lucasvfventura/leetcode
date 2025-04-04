class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check_pal(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check_pal(start , start + length):
                    return s[start : start + length]
            
        return ""