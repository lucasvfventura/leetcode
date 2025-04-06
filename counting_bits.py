class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        output = [0, 1]
        current_power = 1
        for i in range(2, n+1):
            if current_power * 2 == i:
                current_power = i
                output.append(1)
            else:
                output.append(1 + output[i - current_power])
                
        return output
