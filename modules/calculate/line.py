def negative(n):
    if n > 0:
        return abs(n)
    else:
        return -n
class line(object):
    def __init__(self,a,b,grid,name,equation=None):
        self.a,self.b = a.loc,b.loc
        self.grouping = grid.group([a,b],name)
        self.slope = (a[1]-b[1])/(a[0]-b[0])
        self.equation = "y = mx+b"
        self.equation = self.equation.replace("m",str(slope))
        self.y_inter = a[1]-(a[0]*self.slope) 
        self.equation = self.equation.replace("b",str(y_inter))
        self.x_inter = negative(y_inter)/slope
    def point_on(self,point):
        if point.loc[0]*self.slope)+self.y_inter == point.loc[1]:
            return True
        return False
    
        
