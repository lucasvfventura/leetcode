class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """     
        max_length = 0
        i = 0
        j = 0
        chars = {}
        
        while j < len(s):
            char = s[j]
            char_index = chars.get(char)
            if char_index >= i:
                length = j - i
                i = char_index + 1
                if length > max_length:
                    max_length = length

            chars[char] = j
            j += 1
        
        if max_length == 0:
            return len(s)
        
        if j == len(s) and j - i > max_length:
            return j - i 

        return max_length