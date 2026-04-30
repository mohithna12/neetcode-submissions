class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for x in range(len(s)):
            countS[s[x]] = countS.get(s[x], 0) + 1 
            countT[t[x]] = countT.get(t[x], 0) + 1
    
        return countS == countT
        
