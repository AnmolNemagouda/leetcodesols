class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        """
        s=list(s)
        s1=""
        a=0
        for i in s:
            if i.isupper():
                a=ord(i)
                a+=32
                s1+=chr(a)
            else:
                s1+=i
        return s1
        """