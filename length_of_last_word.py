class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1

        while s[i] == ' ':
            i -=1
        last_index = i

        while i >= 0 and s[i] != ' ':
            i -=1

        return last_index - i