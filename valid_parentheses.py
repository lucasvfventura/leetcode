class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brakets = {'(': True, '[':True, '{': True}
        inverted = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        current_open_brakets = []
        for c in s:
            if open_brakets.get(c):
                current_open_brakets.append(c)
            else:
                if len(current_open_brakets) > 0 and inverted[c] == current_open_brakets[-1]:
                    current_open_brakets.pop()
                else:
                    return False
        
        return len(current_open_brakets) == 0

        