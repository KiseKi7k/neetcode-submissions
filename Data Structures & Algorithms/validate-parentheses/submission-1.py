class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        close_paren = list(paren_map.keys())
        open_paren = list(paren_map.values())

        for c in s:
            if c in open_paren:
                stack.append(c)
            
            if c in close_paren:
                if len(stack) == 0:
                    return False
                    
                last = stack.pop()
                if paren_map[c] != last:
                    return False
        
        return len(stack) == 0
            
            