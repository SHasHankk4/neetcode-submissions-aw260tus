class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for itr in operations:
            if itr=="+":
                stack.append(stack[-1]+stack[-2])
            elif itr=="D":
                stack.append(stack[-1]*2)
            elif itr=="C":
                stack.pop()
            else:
                stack.append(int(itr))
        return sum(stack)