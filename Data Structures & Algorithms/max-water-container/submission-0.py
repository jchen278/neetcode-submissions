class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        maxHeight = 0
        
        L = 0
        R = len(heights) - 1

        while L < R:
            area = (R - L) * min(heights[R],heights[L])
            if area > res:
                res = area
            
            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1

        return res