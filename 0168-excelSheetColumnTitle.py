class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        answerList = []
        while columnNumber > 0:
            columnNumber -= 1
            answerList.append(chr(columnNumber%26 + ord('A')))
            columnNumber//=26
        answer = "".join(reversed(answerList))
        return answer