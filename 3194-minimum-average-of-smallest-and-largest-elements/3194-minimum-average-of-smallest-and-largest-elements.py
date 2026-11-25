class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        min_avg = float("inf")

        while left<right:
            avg = (nums[left] + nums[right])/ 2.0
            if avg < min_avg:
                min_avg = avg
            left+=1
            right-=1
        return min_avg
        