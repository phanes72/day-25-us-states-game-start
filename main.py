import pandas

from map_screen import USMapScreen
from state import State

game_still_on = True
data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)

# Screen
us_map = USMapScreen()
st = State()

# populate user info
while game_still_on:
    answer_state = us_map.get_text_input()
    row = df[df.state == answer_state]

    if row.size > 1:
        us_map.increment_score()
        state_name = row.state.values[0]

        x = row.x.values[0]
        y = row.y.values[0]

        st.write_st(state_name, x, y)
        continue
    game_still_on = False
    us_map.end_game()

us_map.exitonclick()
