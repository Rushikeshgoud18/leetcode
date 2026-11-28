class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        current_sum = 0
        for i in nums:
            current_sum+=i
            result.append(current_sum)
        return result