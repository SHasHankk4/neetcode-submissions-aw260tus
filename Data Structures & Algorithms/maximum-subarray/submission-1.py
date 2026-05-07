class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max=nums[0]
        currSum=0
        for num in nums:
            if currSum<0:
                currSum=0
            currSum+=num
            Max=max(Max,currSum)
        return Max

        