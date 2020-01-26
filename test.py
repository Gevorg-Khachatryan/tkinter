from tkinter import *
from random import randint

root = Tk()
c = Canvas(width=800, height=600, bg="black")
l = 3
for i in range(l):
    j = 10
    c.create_rectangle(0 + i * j, 0, 10 + i * j, 10, fill='green')
c.pack()
x, y = 0, 0


def apple():
    r = randint(1, 10)

    c.create_rectangle(r * 10, r * 10, r * 10 + 10, r * 10 + 10, fill='red')


apple()
t = False


def right(event):
    global x, y
    x, y = 10, 0


def down1(event):
    global x, y

    x, y = 0, 10


def up1(event):
    global x, y

    x, y = 0, -10


def left(event):
    global x, y
    x, y = -10, 0


def pause(event):
    global t

    if t:
        t = False
    else:
        t = True
        move2()


root.bind('<Right>', right)
root.bind('<Down>', down1)
root.bind('<Up>', up1)
root.bind('<Left>', left)
root.bind("<space>", pause)

s = len(c.find_all())


def move2():
    global s, t, l

    if t:
        z = c.coords(l)
        c.move(l, x, y)
        if c.coords(l) == c.coords(l + 1):
            c.itemconfig(l + 1, fill="green")

            l += 1
            apple()
        for i in range(l - 1, 0, -1):
            m = c.coords(i)
            c.coords(i, z[0], z[1], z[2], z[3])
            z = m

        for i in range(l, 0, -1):
            if c.coords(i)[0] < 0:
                c.move(i, 800, 0)
            if c.coords(i)[1] < 0:
                c.move(i, 0, 600)
            if c.coords(i)[1] > 600:
                c.move(i, 0, -700)
            if c.coords(i)[0] > 800:
                c.move(i, 0, 700)
        root.after(500, move2)


print(c.find_all())

move2()

root.mainloop()
