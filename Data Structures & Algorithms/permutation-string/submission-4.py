class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if len(s2) < n:
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        for a in range(n):
            counts1[ord(s1[a]) - ord("a")] += 1
            counts2[ord(s2[a]) - ord("a")] += 1
        
        if counts2 == counts1:
            return True

        for i in range(n, len(s2)):
            counts2[ord(s2[i]) - ord("a")] +=1
            counts2[ord(s2[i - n]) - ord("a")] -=1

            if counts2 == counts1:
                return True
        return False


        
        
