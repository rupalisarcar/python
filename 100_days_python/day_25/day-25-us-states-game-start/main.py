import turtle
import os
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

file_path = os.path.dirname(os.path.abspath(__file__))
new_image_path = os.path.join(file_path,"blank_states_img.gif")
screen.addshape(new_image_path)

turtle.shape(new_image_path)

new_csv_file_path = os.path.join(file_path,"50_states.csv")
states_file = pandas.read_csv(new_csv_file_path) 

state_list = states_file["state"].to_list()
print(state_list)

guesed_state = []
unguessed_state = []
while len(guesed_state)<50 :

    ans_state = screen.textinput(title=f"{len(guesed_state)}/50 States Correct", prompt="What's another state's name?").title()

    right_ans = states_file[states_file["state"] == ans_state]

    if ans_state == "Exit":
        new_path = os.path.join(file_path,"ungessed_states.csv")
        # unguessed_state = set(state_list) - set(guesed_state)
        # for state in state_list:
        #     if state not in guesed_state:
        #         unguessed_state.append(state)
        unguessed_state = [state for state in state_list if state not in guesed_state]        
        data = pandas.DataFrame(unguessed_state)        
        data.to_csv(new_path)
        break

    if not right_ans.empty:        
        x = int(right_ans["x"].iloc[0])
        y = int(right_ans["y"].iloc[0])

        guesed_state.append(ans_state)

        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
       
        writer.goto(x,y)
        writer.write(f"{ans_state}", align="center", font=("Courier",10, "normal"))

