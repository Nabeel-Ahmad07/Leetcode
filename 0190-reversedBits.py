class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        for _ in range(32):
            answer = (answer << 1) | (n & 1)
            n >>= 1
        return answer