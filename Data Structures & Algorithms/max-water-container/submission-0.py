class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def get_water():
            return (r - l) * min(heights[r], heights[l])

        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            max_water = max(get_water(), max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water