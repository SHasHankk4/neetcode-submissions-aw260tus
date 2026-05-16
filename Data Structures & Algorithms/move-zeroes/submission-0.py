class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)
        i=0
        while i<r:
            if nums[i]!=0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
            i+=1

        