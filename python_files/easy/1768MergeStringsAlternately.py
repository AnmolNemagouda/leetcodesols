class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=""
        count1=0
        count2=0
        b=len(word1)
        c=len(word2)
        for i in range(0,b+c):
            if i%2==0 and count1<b:
                a+=word1[count1]
                count1+=1
            elif i%2!=0 and count2<c:
                a+=word2[count2]
                count2+=1
        print(a)
        if count1<b:
            x=b-count1
            x=b-x
            a+=word1[x:]
        if count2<c:
            y=c-count2
            y=c-y
            a+=word2[y:]
        return a
