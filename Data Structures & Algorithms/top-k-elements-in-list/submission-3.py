class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counter[n] += 1
        for n, c in counter.items():
            freq[c].append(n)
        
        res = []
        for n in freq[::-1]:
            if len(res) >= k:
                return res
            res += n
        return res