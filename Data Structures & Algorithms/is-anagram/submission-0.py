class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        length = len(s)

        s_counter = {}
        t_counter = {}

        for i in range(length):
            s_char = s[i]
            s_counter[s_char] = s_counter.get(s_char, 0) + 1

            t_char = t[i]
            t_counter[t_char] = t_counter.get(t_char, 0) + 1
        
        return s_counter == t_counter