# hier kommt die GUI rein
from tkinter import *
from Search import Graph


# Erstellung des Roots
root = Tk()
# Größe der Felder
w = 400/20
h = 400/20
# Erstellen des Starts und des Ziels
start = (2,2)
end = (2, 4)

# Erstellen des Spielfelds
## google, wie 2 Dim. Arrays verwaltet werden
# 0 = nichts
# 1 = wall
# 2 = start
# 3 = end
# 4 = Weg von Start zum Ziel

a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

a2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(0,19):
    for j in range(0,19):
        if a[i][j] == 2:
            x = i
            y = j
            start = (x,y)

        elif a[i][j] == 3:
            x = i
            y = j
            end = (x,y)

start = (1,1)
end = (9,6)



# GUI für Algorithmus erstellen
field = Canvas(root, width=400, height=400)
field.pack(side=LEFT)



# Aufteilung der Oberfläche in 2 Bereiche links und Rechts
rightframe = Frame(root)
rightframe.pack(side=RIGHT)



# Methode für den Knopf, um zu reagieren
def startSearch():
    type = optionReturn()
    print(type)

    if type == "A-Star":
        aStar()
        print("A")

    elif type == "dijkstra":
        print("B")
        dijkstra()

# Feld reinigen
def clearField():
    for i in range(0,20):
        for j in range(0, 20):
            a[i][j] = a2[i][j]
    ## Test für a: print(a)
    drawCanvas()

# A-Star Algorithmus aufrufen
def aStar():
    search = Graph()
    path = search.astar(a, start, end)

    for i in range(0, len(path)):
        x = path[i][0]
        y = path[i][1]
        print(x)
        print(y)
        addWay(x,y)

    drawCanvas()
    print(path)

# Dijkstra aufrufen
def dijkstra():
    search = Graph()
    print("Dijkstra start")
    path = search.dijkstra(a,start,end)

    print(path)


# Button hinzufügen
b1 = Button(rightframe, text="Search", fg="Black", command=startSearch)
b2 = Button(rightframe, text="Clear Field", fg="Black", command=clearField)

# Dja
b1.pack()
b2.pack()



# Drop Down hinzufügen
choices = StringVar(root)
choices.set("A-Star")


d1 = OptionMenu(rightframe, choices,"A-Star", "dijkstra", "test2")

# Methode, um die aktuelle Auswahl zu erhalten
def optionReturn():
    print(typ)
    return "A-Star"


d1.pack()


# Maus hinzufügen
def leftClick(event):
    print("Left")
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))
    manageWall(x,y)

    # update der GUI
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

    # Update der GUI
    field.update()
    drawCanvas()

# callback für Aktionen
def callback(event):
    print("mousecursor at" + event.x + " / " + event.y)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))


# Einfügefunktion im Array
def manageWall(x,y):
    x = int(x / 20)
    y = int(y / 20)

    if a[x][y] == 0:
        a[x][y] = 1
    elif a[x][y] == 1:
        a[x][y] = 0

    # Test für die Ausgabe: output()


# Überprüfung der Änderung durch eine Ausgabe
def output():
    for i in range(0, 20):
        l = ""
        for j in range(0, 20):
            erg = a[i][j]
            l += str(erg)
        print(l)


# Löschfunktion im Array
def delete(x,y):
    x = x / 20
    y = y / 20

# Zeichnen der Canvas
# Das ist falsch rum und das Feld passt nicht ganz!!!!
def drawCanvas():

    for y in range(0, 20):
        for x in range(0, 20):
            if a[x][y] == 4:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="lime")
            if a[x][y] == 3:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            if a[x][y] == 2:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            if a[x][y] == 1:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="black")
            if a[x][y] == 0:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="grey")



    x = start[0]
    y = start[1]

    field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")

    x2 = end[0]
    y2 = end[1]

    field.create_rectangle(w * x2, h * y2, w * x2 + 20, h * y2 + 20, fill="green")


# Update a

# Add a way
def addWay(x,y):

    a[x][y] = 4



# Hauptcode

field.bind("<Button-1>", leftClick)
field.bind("<Button-2>", middleClick)
field.bind("<Button-3>", rightClick)

#field.bind("<Motion>", motion)

drawCanvas()
root.mainloop()