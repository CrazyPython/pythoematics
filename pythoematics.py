import grid,calculate
def intlist(l):
    return([int(x) for x in l])
features = ["line calculator"]
prompt = ""
for i in features:
    prompt= prompt + str(features.index(i)),i,"\n"
def lineinter():
    points = raw_input("Enter two points as x1 y1 x2 y2:")
    points = intlist(points.split())
    lowx = min(points[0],points[2])
    highx = max(points[0],points[2])
    lowy = min(points[1],points[3])
    highy = max(points[1],points[3])
    
while True:
    num = raw_input(prompt)
    try:
        num = int(num)
        do = features[num-1]
    except ValueError:
        print"Not a number, try again."
    except IndexError:
        print"Not a choice, try again."
