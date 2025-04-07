class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        s_pointer = 0
        for c in t:
            if c == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
        
        return False