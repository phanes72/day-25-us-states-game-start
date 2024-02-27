from turtle import Turtle

height = 500
width = 800
image = "blank_states_img.gif"
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class USMapScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.setup(width, height)

        self.states_guessed = 0
        self.num_of_states = 50
        self.screen.title = "US States Game!!!"

        self.screen.addshape(image)
        self.shape(image)

        self.num_guesses = 0

        self.textinput = self.get_text_input
        self.input_title = "Guess yo ass!!"

    # @property
    def get_text_input(self):
        self.populate_title()
        return self.screen.textinput(title=str(self.input_title), prompt="What's another name of a state")

    def increment_score(self):
        self.states_guessed += 1
        return int(self.states_guessed)

    def populate_title(self):
        self.input_title = str(self.states_guessed) + "/" + str(self.num_of_states)

    def write_state(self, state, x, y):
        self.increment_score()
        # self.clear()
        self.penup()
        self.goto(x, y)
        self.write(state)

    def end_game(self):
        self.screen.clear()
        self.write(f"FINAL SCORE: {self.input_title}", font=FONT, move=False, align=ALIGNMENT)

    def exitonclick(self):
        self.screen.exitonclick()
