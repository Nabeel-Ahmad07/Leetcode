class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        explored = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in explored:
                return [explored[diff], i]
            explored[nums[i]] = i
