import turtle,pandas

screen = turtle.Screen()
screen.title("United States States Game")
image = "us_project/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("us_project/50_states.csv")
score = 0
while 1 == 1:
    title_score = f"{score}/50 Guess The State"
    answer_state = screen.textinput(title=title_score, prompt="Enter a State")
        
    if len(states_data[states_data["state"].str.lower() == answer_state.lower()]) > 0:
        correct_data = states_data[states_data["state"].str.lower() == answer_state.lower()]
        state_name = correct_data.iloc[0, 0]
        state_x = correct_data.iloc[0,1]
        state_y = correct_data.iloc[0,2]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(state_name, align="center", font=("Arial", 10, "normal"))
        score +=1


        

turtle.mainloop()