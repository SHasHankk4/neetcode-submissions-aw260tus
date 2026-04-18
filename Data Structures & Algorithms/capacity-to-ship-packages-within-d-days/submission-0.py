class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def Canship(cap):
            ships=1
            currcap=cap
            for w in weights:
                if currcap-w<0:
                    ships+=1
                    currcap=cap
                currcap-=w
            return ships<=days

        while l<=r:
            m=(l+r)//2
            if Canship(m):
                res=min(res,m)
                r=m-1
            else:l=m+1
        return res

        