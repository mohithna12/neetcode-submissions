class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curMax = 0

        l, r = 0, len(heights) - 1
        
        while l < r:
            test = (r-l) * min(heights[l], heights[r])
            curMax = max(test, curMax)
            
            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
        
        return curMax