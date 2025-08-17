class Solution:
    def maximum69Number (self, num: int) -> int:
        new=list(str(num))
        num=list(str(num))
        for i in range(0,len(new)):
            if new[i]!='9':
                num.pop(i)
                num.insert(i,'9')
                break
        a=''.join(num)
        return int(a)
                