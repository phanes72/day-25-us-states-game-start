import pandas
from screen import USMapScreen
from state import State

game_still_on = True
data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

# Screen
us_map = USMapScreen()
st = State()

# Get user info


# populate user info
while game_still_on:
    answer_state = us_map.get_text_input()
    row = df[df.state == answer_state]
    state = row.state.values[0]
    x = row.x.values[0]
    y = row.y.values[0]

    st.write_st(state, x, y)

    print(f"state={state}, x={x}, y={y}")

us_map.exitonclick()
