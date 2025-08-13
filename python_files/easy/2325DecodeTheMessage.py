class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k=key.replace(" ","")
        k=list(k)
        counts={}
        j=0
        for i in range(0,len(k)):
            if k[i] not in counts:
                counts[k[i]]=string.ascii_lowercase[j]
                j+=1
            else:
                continue
        m=list(message)
        ans=""
        for i in m:
            if i in counts:
                ans+=counts[i]
            elif i == " ":
                ans+=" "


        return ans