import pandas
from screen import USMapScreen

game_still_on = True
data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

# Screen
us_map = USMapScreen()

# Get user info
answer_state = us_map.get_text_input()
row = df[df.state == answer_state]

# populate user info
state = row.state.values[0]
x = row.x.values[0]
y = row.y.values[0]

print(f"state={state}, x={x}, y={y}")

us_map.exitonclick()
