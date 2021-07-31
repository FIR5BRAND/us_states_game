import turtle
import pandas

screen = turtle.Screen()
screen.title("u.s.states.game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # by using below method & conditions we can get the on click coordinates of the turtle screen
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()


# this is first type of method we use to built us_states_game
# state_name = turtle.Turtle()
# state_name.hideturtle()
# state_name.penup()
# data = pandas.read_csv("50_states.csv")
# data_dict = data.to_dict()
# score = 0
# while True:
#     screen.update()
#     user_answer = screen.textinput(title=f"{score}/50States Correct", prompt="enter a state name in u.s").title()
#     if user_answer == "Exit":
#         break
#     for i in range(len(data_dict["state"])):
#         if data_dict["state"][i] == user_answer:
#             score += 1
#             x = int(data_dict["x"][i])
#             y = int(data_dict["y"][i])
#             state_name.goto(x, y)
#             state_name.write(user_answer, align="left", font=("Arial", 8, "normal"))


# second type
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50States Correct", prompt="enter a state name in u.s").title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)


