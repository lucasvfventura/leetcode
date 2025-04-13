class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanup = []
        for c in s:
            if c.isalnum():
                cleanup.append(c.lower())

        return cleanup == cleanup[::-1]