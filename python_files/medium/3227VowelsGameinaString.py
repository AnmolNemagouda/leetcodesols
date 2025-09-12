class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if 'a' in s:
            return True
        elif 'e' in s:
            return True
        elif 'i' in s:
            return True
        elif 'o' in s:
            return True
        elif 'u' in s:
            return True
        return False