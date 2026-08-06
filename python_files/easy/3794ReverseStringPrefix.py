class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        news=[]
   
        for i in range(k):
            news.insert(0,s[i])
        news.append(s[k:])
        stra="".join(news)
        return stra