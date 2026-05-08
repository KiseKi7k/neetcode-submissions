class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list) # counter -> str[]
        start = ord('a')

        for string in strs:
            counter = [0] * 26
            for char in string:
                counter[ord(char) - start] += 1
            
            group[tuple(counter)].append(string)
                    
        return list(group.values())