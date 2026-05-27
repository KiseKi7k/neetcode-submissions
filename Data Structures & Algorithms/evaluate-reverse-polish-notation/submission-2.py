class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                print(stack, t)
                n2 = stack.pop()
                n1 = stack.pop()
                
                val = 0
                if t == "+":
                    val = n1 + n2
                elif t == "-":
                    val = n1 - n2
                elif t == "*":
                    val = n1 * n2
                elif t == "/":
                    val = int(n1 / n2)
                
                stack.append(val)
                print(stack)

            else:
                stack.append(int(t))
        
        return stack[-1]