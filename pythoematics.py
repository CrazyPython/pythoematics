import sys,os
wd = os.getcwd()
sys.path.extend[wd+"\calculate",wd+"\helper"]
def intlist(l):
    return([int(x) for x in l])
features = ["line calculator"]
prompt = ""
for i in features:
    prompt= prompt + str(features.index(i)),i,"\n"
def lineinter():
    import line
    prompt = \
    """
    1 view all details
    2 view x-intercept
    3 view y-intercept
    4 view equation
    5 view slope
    6 create new line
    7 exit
    """
    choice = 6
    def act(choice):
        if choice == 1:
            act(2)
            act(3)
            act(4)
            act(5)
        elif choice == 2:
            print "x-intercept:"+line.x_inter
        elif choice == 3:
            print "y-intercept:"+line.y_inter
        elif choice == 4:
            print "equation:"+line.equation
        elif choice == 5:
            print "slope:"+line.slope
        elif choice == 6:
            points = raw_input("Enter two points as x1 y1 x2 y2:")
            points = intlist(points.split())
            lowx = min(points[0],points[2])
            highx = max(points[0],points[2])
            lowy = min(points[1],points[3])
            highy = max(points[1],points[3])
            grid = grid.grid([lowx,lowy,highx,highy])
            line = line.line(a,b,grid,"line")
            return grid,line
        elif choice == 7:
            return
        else:
            raise IndexError()
    print prompt
    while True:
        num = raw_input()
        try:
            num = int(num)
            info = act(num)
        except ValueError:
            print"Not a number, try again."
            continue
        except IndexError:
            print"Not a choice, try again."
            continue
        if num == 6:
            grid = info[0]
            line = info[1]
        elif num == 7:
            return
        print prompt
    line =  line
print prompt
while True:
    num = raw_input()
    try:
        num = int(num)
        do = features[num-1]
    except ValueError:
        print"Not a number, try again."
        continue
    except IndexError:
        print"Not a choice, try again."
        continue
    if do == 0:
        lineinter()
    print prompt
