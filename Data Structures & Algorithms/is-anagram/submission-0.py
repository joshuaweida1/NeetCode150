class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        needed = {}
        for i in s:
            needed[i] = needed.get(i, 0) + 1
        for i in t:
            if i not in needed:
                return False
            needed[i] -= 1
            if needed[i] < 0:
                return False
        return True