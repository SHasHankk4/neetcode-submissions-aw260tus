class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_trust=defaultdict(int)
        in_trust=defaultdict(int)

        for i,j in trust:
            out_trust[i]+=1
            in_trust[j]+=1
        for i in range(1,n+1):
            if out_trust[i]==0 and in_trust[i]==n-1:
                return i
        return -1