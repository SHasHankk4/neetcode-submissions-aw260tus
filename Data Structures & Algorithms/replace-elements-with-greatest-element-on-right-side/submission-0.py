class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        Maxright=-1
        for i in range(n-1,-1,-1):
            res[i]=Maxright
            Maxright=max(arr[i],Maxright)
        return res

        