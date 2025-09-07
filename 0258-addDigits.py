class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10
            num = digitSum 

        return num