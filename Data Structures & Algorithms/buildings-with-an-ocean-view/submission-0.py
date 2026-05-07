class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        j=len(heights)-1
        res=[j]
        while j>=0:
            if heights[j]>heights[res[-1]]:
                res.append(j)
            j-=1
        res.reverse()
        return res

