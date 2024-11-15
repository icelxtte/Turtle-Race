import turtle
import random
import time

# Setting up the screen and turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
t.pensize(5)
t.speed(10)
t.color("white")
t.penup()
t.goto(0, 180)
t.write("Fastest Turtle Race Ever", align='center', font=("Arial", 24, "bold"))
t.penup()
t.goto(0, 150)
t.write("Who will get fishy first?????", align='center', font=("Arial", 14, "bold"))

# Countdown function
def countdown():
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.goto(0, 250)
    messages = ["Get Ready!", "3", "2", "1", "GO!"]
    for message in messages:
        title_turtle.clear()
        title_turtle.color("red")  # Set the font color to red
        title_turtle.write(message, align="center", font=("Times New Roman", 30, "bold"))
        time.sleep(1)
    title_turtle.clear()

# Drawing the starting and finish lines
# Starting line
t.goto(-200, 150)
t.pendown()
t.goto(-200, 0)
t.penup()

# Finish line
t.goto(200, 150)
t.pendown()
t.goto(200, 0)

# Define Fish turtle
fish = []
y_positions = [130, 100, 70, 40, 10]
for y in y_positions:
    f = turtle.Turtle()
    f.color('orange')
    f.penup()
    f.goto(210, y)
    f.pensize(10)
    f.write("🐟", font=("Arial", 24, "normal"))
    fish.append(f)

# Adding turtles for the race
# Pink turtle
pt = turtle.Turtle()
pt.shape('turtle')
pt.color('pink')
pt.pensize(2)
pt.penup()
pt.goto(-200, 140)
pt.pendown()

# Purple turtle
purt = turtle.Turtle()
purt.shape("turtle")
purt.color('purple')
purt.pensize(2)
purt.penup()
purt.goto(-200, 110)
purt.pendown()

# Gray turtle
grt = turtle.Turtle()
grt.shape('turtle')
grt.color("gray")
grt.pensize(2)
grt.penup()
grt.goto(-200, 80)
grt.pendown()

# Green turtle
gt = turtle.Turtle()
gt.shape("turtle")
gt.color("green")
gt.pensize(2)
gt.penup()
gt.goto(-200, 50)
gt.pendown()

# Black turtle
bt = turtle.Turtle()
bt.shape("turtle")
bt.color("black")
bt.pensize(2)
bt.penup()
bt.goto(-200, 20)
bt.pendown()

# Function to flash the fish (emoji)
def flashFish(winner_index):
    fish[winner_index].clear()  # Clear any previous drawing of fish emoji
    for _ in range(100):  # Flash many times
        fish[winner_index].write("🐟", font=("Arial", 24, "normal"))
        time.sleep(0.5)
        fish[winner_index].clear()  # Clear the fish emoji
        time.sleep(0.5)
    fish[winner_index].write("🐟", font=("Arial", 24, "normal"))  # Keep the fish visible after the flashing

# Start the countdown
countdown()

# Starting the race
while True:
    pt.forward(random.randint(1, 10))
    purt.forward(random.randint(1, 10))
    grt.forward(random.randint(1, 10))
    gt.forward(random.randint(1, 10))
    bt.forward(random.randint(1, 10))

    if pt.xcor() > 200:
        print("Pink Turtle Wins Fishy!")
        t.penup()
        t.goto(0, -50)
        t.color("pink")
        t.write("Pink Turtle Wins Fishy!", align="center", font=("Arial", 32, "bold"))
        flashFish(0)  # Flash the fish at the first position
        time.sleep(7)
        break
    elif purt.xcor() > 200:
        print("Purple Turtle Wins Fishy!")
        t.penup()
        t.goto(0, -50)
        t.color("purple")
        t.write("Purple Turtle Wins Fishy!", align="center", font=("Arial", 32, "bold"))
        flashFish(1)  # Flash the fish at the second position
        time.sleep(7)
        break
    elif gt.xcor() > 200:
        print("Green Turtle Wins Fishy!")
        t.penup()
        t.goto(0, -50)
        t.color("green")
        t.write("Green Turtle Wins Fishy!", align="center", font=("Arial", 32, "bold"))
        flashFish(2)  # Flash the fish at the third position
        time.sleep(7)
        break
    elif grt.xcor() > 200:
        print("Gray Turtle Wins Fishy!")
        t.penup()
        t.goto(0, -50)
        t.color("gray")
        t.write("Gray Turtle Wins Fishy!", align="center", font=("Arial", 32, "bold"))
        flashFish(3)  # Flash the fish at the fourth position
        time.sleep(7)
        break
    elif bt.xcor() > 200:
        print("Black Turtle Wins Fishy!")
        t.penup()
        t.goto(0, -50)
        t.color("black")
        t.write("Black Turtle Wins Fishy!", align="center", font=("Arial", 32, "bold"))
        flashFish(4)  # Flash the fish at the fifth position
        time.sleep(7)
        break
