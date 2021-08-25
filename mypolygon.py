import turtle


def square(t, length):
    for i in range(0, 4):
        bob.lt(90)
        bob.fd(length)
    # bob.fd(100)

    t.mainloop()


def polygon(t, length, sides):
    for i in range(0, sides):
        bob.lt(360 / sides)
        bob.fd(length)
    # bob.fd(100)

    t.mainloop()


def circle(t, r):
    polygon(t, )


bob = turtle.Turtle()

# square(bob, 200)
polygon(bob, 200, 6)
