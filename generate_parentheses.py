class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        substrings = [(0, 0, '')]

        output = []
        while substrings:
            (total, closed, sub) = substrings.pop()

            if len(sub) == n *2:
                output.append(sub)

            if total < n:
                substrings.append((total + 1, closed, sub + '('))
            
            if total > closed:
                substrings.append((total, closed + 1, sub + ')'))

        return output