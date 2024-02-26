import turtle
import pandas

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

# Screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# Get user info
answer_state = screen.textinput(title="Guess the State", prompt="What's another name of a state")
row = df[df.state == answer_state]

# populate user info
state = row.state.values[0]
x = row.x.values[0]
y = row.y.values[0]

print(f"state={state}, x={x}, y={y}")

screen.exitonclick()
