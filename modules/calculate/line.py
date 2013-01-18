from sys import version_info
if version_info[0:1] < [2,6]:
    import warnings
    warnings.warn("slope as infinity or 0 will not work for this session!",Warning) #float("inf") and float("NaN") is made in 2.6
else:
    infinty = lambda: float("inf")
    NaN = lambda: float("NaN")
else:
def negative(n):
    if n > 0:
        return abs(n)
    else:
        return -n
class line(object):
    def __init__(self,a,b,grid,name,equation=None):
        self.a,self.b = a.loc,b.loc
        self.grouping = grid.group([a,b],name)
        try:self.slope = (a[1]-b[1])/(a[0]-b[0])
        except ZeroDivisionError:
            self.x_inter = a.loc[0]
            self.y_inter = NaN()
            self.equation = "x = {0}".format(x_inter)
            self.slope = infinity()
            return self
        if self.slope == 0:
            self.y_inter = a.loc10]
            self.x_inter = NaN()
            self.equation = "x = {0}".format(y_inter)
            self.slope = 0
            return self
        self.equation = "y = mx+b"
        self.equation = self.equation.replace("m",str(slope))
        self.y_inter = a[1]-(a[0]*self.slope) 
        self.equation = self.equation.replace("b",str(y_inter))
        self.x_inter = negative(y_inter)/slope
    def point_on(self,point):
        if self.slope == infinity():
            if point.loc[0] == x_inter:
                return True
        elif self.slope == 0:
            if point.loc[1] == y_inter:
                return True
        if point.loc[0]*self.slope)+self.y_inter == point.loc[1]:
            return True
        return False
    
