class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))
        if len(sortedS) != len(sortedT):
            return False;
        for i in range(len(s)):
            if sortedS[i] != sortedT[i]:
                return False;
        return True;