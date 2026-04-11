import math
class phan_so :
    def __init__(self,mau=1,tu=0):
        self.mau=mau
        self.tu=tu
    def __str__(self):
        return f'{self.tu}/{self.mau}'