class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dia=-inf
        m=[0]
        for i in dimensions:
            j=[]
            j.append(i)
            for k in j:
                
                ini = sqrt((int(k[0])**2+(int(k[1])**2)))
                if ini>=dia:
                    if ini==dia:            
                        n=k[0]*k[1]
                        if n>m[0]:
                            dia=ini
                            m.pop(0)
                            m.append(n)
                    elif ini>dia:
                        dia=ini
                        n=k[0]*k[1]
                        m.pop(0)
                        m.append(n)
                    

        return m[0]
