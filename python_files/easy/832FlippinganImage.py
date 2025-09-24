class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(image)):
            a=image[i]
            a=a[::-1]
            image.pop(i)
            for j in range(0,len(a)):
                if a[j]==1:
                    a.pop(j)
                    a.insert(j,0)
                elif a[j]==0:
                    a.pop(j)
                    a.insert(j,1)
            image.insert(i,a)
        return image
