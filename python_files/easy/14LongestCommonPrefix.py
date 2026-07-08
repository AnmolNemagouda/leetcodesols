class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        res=a
        i=1
        while i<len(strs):
            cur=""
            k=strs[i]
            for j in range(0,len(res)):
                if j<len(k):
                    if res[j]!=k[j]:
                        break
                    else:
                        cur+=res[j]

            if cur<=res:
                res=cur
            i+=1
        return res


        