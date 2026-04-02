class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for itr in range (len(s)):
            countS[s[itr]] = countS.get(s[itr], 0) + 1
            countT[t[itr]] = countT.get(t[itr], 0) + 1
        return countS==countT