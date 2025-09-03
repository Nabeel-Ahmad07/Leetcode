class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}

        for elem in nums:
            if elem in count:
                return True
            else:
                count[elem] = 1
        return False