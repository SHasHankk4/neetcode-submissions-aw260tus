class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Max_water=0
        i,j=0,len(heights)-1
        while i<j:
            Area=(j-i)*min(heights[i],heights[j])
            Max_water=max(Max_water,Area)
            if heights[j]>=heights[i]:
                i+=1
            else:
                j-=1
            
        return Max_water
        
        