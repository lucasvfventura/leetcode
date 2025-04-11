class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        current = grid
        infected = True
        minutes = 0
        while infected:
            infected = False
            next_grid = [[j for j in i] for i in current]
            for i in range(0, len(current)):
                for j in range(0, len(current[i])):
                    if current[i][j] == 2:
                        if i > 0 and current[i-1][j] == 1:
                            infected = True
                            next_grid[i-1][j] = 2

                        if i + 1 < len(current) and current[i+1][j] == 1:
                            infected = True
                            next_grid[i+1][j] = 2

                        if j > 0 and current[i][j-1] == 1:
                            infected = True
                            next_grid[i][j-1] = 2

                        if j + 1 < len(current[i]) and current[i][j+1] == 1:
                            infected = True
                            next_grid[i][j+1] = 2
                    
            current = next_grid
            minutes += 1
        
        for i in range(0, len(current)):
            for j in range(0, len(current[i])):
                if current[i][j] == 1:
                    return -1

        return minutes - 1