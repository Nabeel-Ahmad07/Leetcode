class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        answer = 0
        for c in columnTitle:
            answer = answer *26 + (ord(c) - ord('A') +1)
        return answer