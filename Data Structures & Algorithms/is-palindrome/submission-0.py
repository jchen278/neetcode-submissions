class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for i in range(len(s)):
            if s[i].isalnum():
                filtered += s[i]
        filtered=filtered.lower()
        reverseFiltered = ""
        for char in filtered:
            reverseFiltered = char + reverseFiltered
        print(reverseFiltered)
        return filtered==reverseFiltered