class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def maxElement(nums):
            Max=float("-inf")
            i=0
            while i<len(nums):
                Max=max(Max,nums[i])
                i+=1
            return Max
        i=0
        j=k-1
        res=[]
        while j<len(nums):
            res.append(maxElement(nums[i:j+1]))
            i+=1
            j+=1
        return res


