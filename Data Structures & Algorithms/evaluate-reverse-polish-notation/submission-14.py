class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if (tokens[i]!= "+" and tokens[i]!= "-" and tokens[i]!= "/" and tokens[i]!= "*"):
                hold = int(tokens[i])
                stack.append(hold)
            elif tokens[i]=="+":
               b = stack.pop()
               a = stack.pop()
               stack.append(a + b)
            elif tokens[i]=="-":
               b = stack.pop()
               a = stack.pop()
               stack.append(a - b)
            elif tokens[i]=="*":
               b = stack.pop()
               a = stack.pop()
               stack.append(a * b)
            elif tokens[i]=="/":
               b = stack.pop()
               a = stack.pop()
               stack.append(int(a/b))
        return stack[0]
            

