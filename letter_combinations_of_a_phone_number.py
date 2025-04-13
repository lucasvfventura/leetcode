class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if digits == "":
            return []

        output = chars[digits[0]]
        for i in range(1, len(digits)):
            new_output = []
            for word in output:
                for char in chars[digits[i]]:
                    new_output.append(word + char)
            output = new_output

        return output
        