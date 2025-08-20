class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2

        x,y = 1,2
        for _ in range(2, n):
            z = x+y
            x=y
            y=z
        
        return y
            