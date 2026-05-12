class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        max1=0
        for num in nums:
            if num==1:
                res+=1
                max1=max(res,max1)
            else:
                
                res=0
        return max1
        