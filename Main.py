
from tkinter import *
from Search import Graph

root = Tk()
# Size of the field
w = 400/20
h = 400/20

# Set start and goal
start = (1,1)
end = (18, 18)

# Field description
# 0 = nothing
# 1 = constructed wall
# 2 = start
# 3 = end
# 4 = pathfinding way
# 5 = surrounding Wall

# Main field
a  = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
     [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]


# Define the overall guy
field = Canvas(root, width=400, height=400)
field.pack(side=LEFT)

# Separate the guy
rightframe = Frame(root)
rightframe.pack(side=RIGHT)


# Defines which algorithm is executed
def startSearch():
    b1['state'] = 'disabled'
    type = optionReturn()
    print(type)

    if type == "A-Star":
        aStar()
        print("A")

    elif type == "dijkstra":
        print("B")
        dijkstra()

    elif type == "BFSearch":
        bfsearch()
        print("C")

# Clear Field except wall
def clearField():
    for i in range(1,19):
        for j in range(1, 19):
                a[i][j] = 0
    drawCanvas()
    b1['state'] = 'normal'

#clear only algorithm, leave constructed walls
def partialClear():
    for i in range(1,19):
        for j in range(1, 19):
            if a[i][j] == 4:
                a[i][j] = 0
    drawCanvas()
    b1['state'] = 'normal'

# A-Star
def aStar():
    print("A* Search start")
    search = Graph()
    path = search.astar(a, start, end)

    drawCanvas()
    print("Test")

    if not path:
        print("path is empty")
    else:

        for i in range(0, len(path)):
            x = path[i][0]
            y = path[i][1]
            print(x)
            print(y)
            addWay(x,y)

        drawCanvas()
        print(path)

# Dijkstra
def dijkstra():
    search = Graph()
    path = search.dijkstra2(a,start,end)

    print("Dijkstra start")

    for i in range(0, len(path)):
        x = path[i][0]
        y = path[i][1]
        print(x)
        print(y)
        addWay(x,y)

    drawCanvas()
    print(path)

#Breadth First
def bfsearch():
    b1.setEnabled(False)
    search = Graph()
    path = search.bfsearch(a, start, end)

    print("Breadth First Search start")

    for i in range(0, len(path)):
        x = path[i][0]
        y = path[i][1]
        print(x)
        print(y)
        addWay(x, y)

    drawCanvas()
    print(path)



#add buttons
b1 = Button(rightframe, text="Search", fg="Black", command=startSearch, state='normal')
b2 = Button(rightframe, text="Clear Field", fg="Black", command=clearField)
b4 = Button(rightframe, text="Partial Clear", fg="Black", command=partialClear)
b3 = Button(rightframe, text="End application", fg="Black", command=root.destroy)


#adding the drop-down
variable = StringVar(root)
# default value
variable.set("A-Star")
d1 = OptionMenu(rightframe, variable,"A-Star", "dijkstra", "breadth first")


#returning the highlighted choice
def optionReturn():
    print("value is: ", variable.get())
    return variable.get()

# include forms on the canvas (rightframe)
b1.pack()
b2.pack()
b4.pack()
d1.pack()
b3.pack()

# add the mouse events
def leftClick(event):
    print("Left")
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))
    manageWall(x,y)

    # update the GUI
    field.update()
    drawCanvas()

def middleClick(event):
    print("Middle")
    x, y = event.x, event.y
    end = (x, y)

    drawCanvas()


def rightClick(event):
    print("Right")
    x, y = event.x, event.y
    x = int(x/20)
    y = int(y/20)
    end = (x, y)
    print(end)

# update guy
    field.update()
    drawCanvas()

# callback for actions
def callback(event):
    print("mousecursor at" + event.x + " / " + event.y)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))


# include constructed walls into field
def manageWall(x,y):
    x = int(x / 20)
    y = int(y / 20)

    if a[x][y] == 0:
        a[x][y] = 1
    elif a[x][y] == 1:
        a[x][y] = 0
# can also change the path to wall
    elif a[x][y] == 4:
        a[x][y] = 1


# check changes through output
def output():
    for i in range(0, 20):
        l = ""
        for j in range(0, 20):
            erg = a[i][j]
            l += str(erg)
        print(l)


# function to delete
def delete(x,y):
    x = x / 20
    y = y / 20

# draw canvas
def drawCanvas():
    for y in range(0, 20):
        for x in range(0, 20):
            if a[x][y] == 4:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="lime")
            elif a[x][y] == 3:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            elif a[x][y] == 2:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            elif a[x][y] == 1:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="black")
            elif a[x][y] == 0:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="grey")
            elif a[x][y] == 5:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="black")

# adding start- and endpoint
    x = start[0]
    y = start[1]
    field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")

    x2 = end[0]
    y2 = end[1]
    field.create_rectangle(w * x2, h * y2, w * x2 + 20, h * y2 + 20, fill="green")

# Add a way
def addWay(x,y):
    a[x][y] = 4

field.bind("<Button-1>", leftClick)
field.bind("<Button-2>", middleClick)
field.bind("<Button-3>", rightClick)

drawCanvas()
root.mainloop()