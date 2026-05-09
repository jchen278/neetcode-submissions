class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictKeys = {}
        for x in strs:
            key = ''.join(sorted(x))
            if key not in dictKeys:
                dictKeys[key] = []
            dictKeys[key].append(x)
        return list(dictKeys.values())
