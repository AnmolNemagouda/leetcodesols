class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s=coordinates
        s=list(s)
        if (s[0]=='a' or s[0]=='c' or s[0]=='e' or s[0]=='g') and (int(s[1])%2!=0):
            return False
        elif (s[0]=='a' or s[0]=='c' or s[0]=='e' or s[0]=='g') and (int(s[1])%2==0):
            return True
        elif (s[0]=='b' or s[0]=='d' or s[0]=='f' or s[0]=='h') and (int(s[1])%2!=0):
            return True
        else:
            return False