class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = [[0]*len(i) for i in grid]

        for i in range(len(grid)):
            for j, val in enumerate(grid[i]):
                if i == 0 and j == 0:
                    output[i][j] = val
                elif i == 0:
                    output[i][j] = val + output[i][j-1]
                elif j == 0:
                    output[i][j] = val + output[i-1][j]
                else:
                    output[i][j] = val + min(output[i-1][j], output[i][j-1])
        
        return output[-1][-1]