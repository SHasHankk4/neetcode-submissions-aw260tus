class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char={}
        res=0
        i=0
        for j in range(len(s)):
            char[s[j]]=1+char.get(s[j],0)
            if (j-i+1)-max(char.values())<=k:
                res=max(res,(j-i+1))
            else:
                char[s[i]]-=1
                i+=1    
            
        return res

        