class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        charset=set()
        i=0
        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1
            charset.add(s[j])
            res=max(j-i+1,res)
        return res

        