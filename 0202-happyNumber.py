class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqrSum(num):
            total = 0
            while num > 0:
                digit = num%10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sqrSum(n)
        return n == 1
