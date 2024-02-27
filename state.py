from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def write_st(self, state, x, y):
        self.goto(x, y)
        self.write(state, font=FONT, move=False, align=ALIGNMENT)
