class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = []
        b = []
        c = ''
        d = ''

        for i in version1:
            if i == '.':
                if c != '':
                    a.append(int(c))
                    c = ''
            else:     
                c += i
        if c != '':
            a.append(int(c))
        for i in version2:
            if i == '.':
                if d != '':
                    b.append(int(d))
                    d = ''       
            else:
                d += i
        if d != '':
            b.append(int(d))
        n = max(len(a), len(b))
        a.extend([0] * (n - len(a)))
        b.extend([0] * (n - len(b)))
        for i in range(n):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        return 0
        