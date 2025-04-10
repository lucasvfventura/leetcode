class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        j = 0
        i = 0
        k = 0
        visited = -111
        m = len(matrix)
        n = len(matrix[0])
        output = [0]*(m*n)

        if m == 1 and n == 1:
            return matrix[0]

        current_direction = 'right'
        
        while i >= 0 and i < m and j >= 0 and j < n and matrix[i][j] != visited:
            output[k] = matrix[i][j]
            k += 1
            matrix[i][j] = visited

            if current_direction == 'right':
                if j < n - 1 and matrix[i][j+1] != visited:
                    j += 1
                else:
                    i += 1
                    current_direction = 'down'
            elif current_direction == 'down':
                if i < m - 1 and matrix[i+1][j] != visited:
                    i += 1
                else:
                    j -= 1
                    current_direction = 'left'
            elif current_direction == 'left':
                if j > 0 and matrix[i][j-1] != visited:
                    j -= 1
                else:
                    i -= 1
                    current_direction = 'up'
            else:
                if i > 0  and matrix[i-1][j] != visited:
                    i -= 1
                else:
                    j += 1
                    current_direction = 'right'

        return output