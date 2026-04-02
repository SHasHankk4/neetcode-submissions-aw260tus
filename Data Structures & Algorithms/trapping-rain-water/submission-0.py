class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        i,j=0,len(height)-1
        res=0
        maxl,maxr=height[i],height[j]
        while i<j:
            if maxl<maxr:
                i+=1
                maxl=max(maxl,height[i])
                res+=maxl-height[i]
            else:
                j-=1
                maxr=max(maxr,height[j])
                res+=maxr-height[j]
        return res