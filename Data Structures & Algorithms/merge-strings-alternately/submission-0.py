class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        i=j=0
        string=""
        while i<n or j<m:
            if i<n:
                string+=word1[i]
            if j<m:
                string+=word2[j]
            i+=1
            j+=1
        return string

        