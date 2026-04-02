class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        Bracket_Map={")":"(","}":"{","]":"["}
        for c in s:
            if c in Bracket_Map:
                if stack and stack[-1]==Bracket_Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else: return False
        