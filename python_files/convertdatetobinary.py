class Solution:
    def convertDateToBinary(self, date: str) -> str:
        yyyy,mm,dd=date.split("-")
        yyyy=bin(int(yyyy))
        mm=bin(int(mm))
        dd=bin(int(dd))
        return f"{yyyy[2:]}-{mm[2:]}-{dd[2:]}"
        