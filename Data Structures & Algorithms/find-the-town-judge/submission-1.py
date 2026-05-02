class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score=defaultdict(int)
        for i,j in trust:
            trust_score[i]-=1
            trust_score[j]+=1
        for i in range(1,n+1):
            if trust_score[i]==n-1:
                return i
        return -1