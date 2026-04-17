class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l,r=0,num//2
        
        while l<=r:
            mid=(l+r)//2
            check=mid*mid
            if check>num:
                r=mid-1
            elif check<num:
                l=mid+1
            else:
                return True
        return False
        