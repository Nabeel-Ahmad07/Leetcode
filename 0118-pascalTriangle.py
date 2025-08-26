class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for rows in range(numRows):
            row = [1]*(rows+1)

            for i in range(1, rows):
                row[i] = triangle[rows-1][i-1] + triangle[rows-1][i]

            triangle.append(row)
        return triangle