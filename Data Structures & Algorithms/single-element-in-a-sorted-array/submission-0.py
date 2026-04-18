class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if (m-1<0 or nums[m]!=nums[m-1]) and ((m==len(nums)-1) or nums[m]!=nums[m+1]):
                return nums[m]
            
            if nums[m]==nums[m-1]:
                size=m-1
            else:
                size=m
            if size%2==1:
                r=m-1
            else:
                l=m+1
            