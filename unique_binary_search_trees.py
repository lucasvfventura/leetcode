class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        dp = [1, 2]
    
        for i in range(2, n):
            count = 0
            for p in range(i+1):
                if p == 0:
                    count += dp[i - 1]
                elif p == i:
                    count += dp[i - 1]
                else:
                    count += dp[p-1]*dp[i-p-1]

            #0 2 2
            # 1 2 
            # 2 2

            dp.append(count)
        
        return dp[-1]