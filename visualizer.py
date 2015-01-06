__author__ = 'Hamid FzM'

import turtle
from random import randint
from timeit import Timer


def diagram():
    pivot = turtle.Turtle()
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

wn = turtle.Screen()
diagram()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-200, -200)
pen.pendown()

for i in xrange(400):
    pen.goto(-200 + i,
             -200 + Timer('quick_sort(%s)' % [randint(0, 5000) for x in xrange(i)], 'from Sort import quick_sort').timeit(number=1) * 100000)


wn.getcanvas().postscript(file="duck.eps")
turtle.done()


