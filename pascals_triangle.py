class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1,1]]
        
        dp = [[1] * i for i in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(1, i//2 + 1):
                dp[i][j] = dp[i -1][j - 1] + dp[i - 1][j]
                dp[i][i - j] = dp[i -1][j - 1] + dp[i - 1][j]

        return dp
