class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        vals = []
        pairs = {'(' : ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in pairs:
                vals.append(s[i])
            else:
                if (not vals or pairs[vals.pop()] != s[i]): return False
        return not vals


