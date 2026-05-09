class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for l in s:
            if l in dictS:
                dictS[l] += 1
            else:
                dictS[l] = 1
        for l in t:
            if l in dictT:
                dictT[l] += 1
            else:
                dictT[l] = 1

        return dictS == dictT
            