import turtle
from turtle import Turtle

height = 500
width = 800
image = "blank_states_img.gif"


class USMapScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        # self.screen.setup(width, height)

        self.states_guessed = -1
        self.num_of_states = 50
        self.screen.title = "US States Game!!!"

        self.screen.addshape(image)
        self.shape(image)

        self.num_guesses = self.increment_score()

        self.textinput = self.get_text_input

    # @property
    def get_text_input(self):
        input_title = "Guess yo ass"  # self.increment_score()
        return self.screen.textinput(title=str(input_title), prompt="What's another name of a state")

    def increment_score(self):
        self.states_guessed += 1
        return int(self.states_guessed)

    def populate_title(self):
        self.increment_score()
        input_title = str(self.states_guessed) + "/" + str(self.num_of_states)
        self.screen.textinput(title=input_title, prompt="What's another name of a state")

    def write_state(self, state, x, y):
        self.clear()
        self.penup()
        self.goto(x, y)
        self.write(state)

        self.populate_title()

    def exitonclick(self):
        self.screen.exitonclick()
