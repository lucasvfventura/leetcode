class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # a b
        # c x
        # x = b + c
        
        positions = [[1]*n for i in range(m)]

        for i in range(0, m):
            for j in range(1, n):
                if i == 0:
                    positions[i][j] = positions[i][j-1]
                else:
                    positions[i][j] = positions[i][j-1] + positions[i-1][j]

        return positions[m - 1][n - 1]

