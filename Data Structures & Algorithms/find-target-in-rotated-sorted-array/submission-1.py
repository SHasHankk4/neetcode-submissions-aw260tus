class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l

        def binSearch(l,r):
            while l<=r:
                mid=(l+r)//2
                if target>nums[mid]:
                    l=mid+1
                elif target<nums[mid]:
                    r=mid-1
                else:
                    return mid
            return -1
        
        result=binSearch(0,pivot-1)
        if result!=-1: return result

        return binSearch(pivot,len(nums)-1)



        