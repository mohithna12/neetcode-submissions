class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        currMin = max(piles)

        

        while l <= r:
            test = 0
            m = (l + r) // 2
            for i in piles:
                test += math.ceil(float(i) / m)
            if test <= h:
                r = m - 1
                currMin = m
            else:
                l = m + 1
            
        return currMin
