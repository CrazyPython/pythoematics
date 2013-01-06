

"version .1 supports __getitem__ and __setitem__ and fill and fillrect"
"version .2 supports __str__ and __dict__"
"""
version .3  
full iteriator support
__len__ and __contains__
added documentation
__setitem__  and __setitem__supports slices with support for versions below 2.0(very unlikley)
"""
"""
version .4
allows grouping of points through 'groups'
able to carry things related to graph
"""
import sys,threading
class i:
    def __init__(self,l):
        self.pos = 0
        self.l = l
    def __iter__(self):
        return self
    def next(self):
        if self.pos == len(self.l):
            raise StopIteration()
        value = self.l[self.pos]
        self.pos += 1
        return value
class point:
    def __init__(self,value,loc,groups = []):
        self.value = value
        self.loc = loc
        self.groups = groups
    def add_group(self,group):
        self.groups.append(group)
class grid:
    """
    mutable object
    deletion not supported(just wacky)
    no order(wacky and uses a dictionary)
    slicing is possible, ignores step
    """
    def _check(self,var):
        if len(var) != 4:
            raise TypeError("size needs to be a length of 4, not "+len(var)+".")
        for i in var:
            if type(i) != int:
                raise TypeError("Every item in size must be a integer")
    def __init__(self,size,default = None,large=False):
        "__init__([lowx,lowy,highx,highy],default=None) --> grid object"
        self._check(size)
        self.lowx = size[0]
        self.lowy = size[1]
        self.highx = size[2]+1
        self.highy = size[3]+1
        self.g = {}
        self.groups = {}
        self.carry = []
        for x in range(self.lowx,self.highx):
            for y in range(self.lowy,self.highy):
                plot(x,y,default)
    def __getitem__(self,arg):
        if type(arg) == slice:
            self._ghelper2(arg.start,arg.stop)
        else:
            return self._ghelper(arg)
    def _ghelper(self,arg):
        return self.g[arg]
    def _ghelper2(self,start,stop):
        ret = []
        for x in range(start[0],stop[0]):
            for y in range(stop[1],start[1]):
                ret.append(self.g[(x,y)])
    def __setitem__(self,a,b):
        if type(a) == slice:
            self.fillrect(slice.start,slice.stop,b)
        else:
            self.fill(a[0],a[1],b)
    def fillrect(self,start,stop,replace):
        for x in range(start[0],stop[0]):
            for y in range(stop[1],start[1]):
                self.plot(x,y,replace)
    def fill(self,replace):
        fillrect((self.lowx,lowy),(self.highx,self.highy),replace)
    def plot(self,x,y,replace):
        self.g[(x,y)] = point(replace,(x,y))
    def group(self,points,name):
        for point in points:
            self.g(point).add_group(name)
    def __str__(self):
        string = "" 
        length = self.minx - maxx
        for entry in self.g:
            thing = self.g[entry]
            string += "["+thing+"]"
            if entry[1] == length:
                string +="/n"
        return string    

    def __repr__(self):
        ret = ""
        keys = self.g.keys()
        keys.sort()
        for i in keys:
            ret += "Point "+str(i)+" with status "+str(self.g[i])+"\n"
        return ret
    def __dict__(self):
        return self.g
    def __len__(self):
        return max(self.g.keys())[0]
    def __iter__(self):
        global i
        l = self.g.values()
        l.sort()
        return i
    def __contains__(self,item):
        return item in self.g
    if sys.version_info < (2, 0):
        def __getslice__(self, i, j):
            return self[max(0, i):max(0, j):]
        def __setslice__(self, i, j, seq):
            self[max(0, i):max(0, j):] = seq
        def __delslice__(self, i, j):
            del self[max(0, i):max(0, j):]
