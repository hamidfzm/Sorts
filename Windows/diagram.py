__author__ = 'Hamid FzM'

# python imports
from random import randint
from timeit import Timer

# tk imports
from Tkinter import Toplevel, Frame, Label, Canvas
import turtle

# project imports
import Sort


class Diagram(Toplevel):
    def __init__(self, master, sorts):
        Toplevel.__init__(self, master)
        self.bind("<Destroy>", self.on_destroy)
        self.grab_set()

        self.withdraw()

        frame = Frame(self, bg='black')
        Label(frame, text=u'Hello', bg='grey', fg='white').pack(fill='x')
        canvas = Canvas(frame, width=800, height=600)
        canvas.pack()
        frame.pack(fill='both', expand=True)

        pivot = turtle.RawTurtle(canvas)
        pivot.penup()
        pivot.goto(-200, -200)

        # draw horizontal edge
        pivot.pendown()
        pivot.fd(420)
        pivot.stamp()

        pivot.penup()
        pivot.setx(-200)

        # draw vertical edge
        pivot.seth(90)
        pivot.pendown()
        pivot.fd(420)
        pivot.stamp()

        del pivot

        pens = list()

        for selected_sort in sorts:
            pen = turtle.RawTurtle(canvas)
            pen.hideturtle()
            pen.penup()
            pen.goto(-200, -200)
            pen.pendown()
            pen.algorithm = Sort.__all__[selected_sort]

            pens.append(pen)

        self.deiconify()

        for i in xrange(400):
            rands = [randint(0, 5000) for x in xrange(i)]
            for pen in pens:
                pen.goto(-200 + i,
                         -200 + Timer('%s(%s)' % (pen.algorithm, rands), 'from Sort import %s' % pen.algorithm).timeit(number=1) * 100000)

    def on_destroy(self, event):
        if event.widget == self:
            self.grab_release()