class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = {}
        for s in magazine:
            chars[s] = chars.get(s, 0) + 1
        
        for s in ransomNote:
            quantity = chars.get(s, 0)
            if quantity == 0:
                return False
            chars[s] = chars[s] - 1
        
        return True