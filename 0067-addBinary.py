class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = format(int(a,2) + int(b,2), 'b')
        return str(result)