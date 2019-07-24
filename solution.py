import turtle
import random

def main():
    #Part A
    window = turtle.Screen()       # 2.  Create a screen
    window.bgcolor('lightblue')

    michelangelo = turtle.Turtle()    # 3.  Create two turtles
    leonardo = turtle.Turtle()
    michelangelo.color('orange')
    leonardo.color('blue')
    leonardo.speed(0)
    michelangelo.shape('turtle')
    leonardo.shape('turtle')


    michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
    leonardo.up()
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)


    # 5. your code goes here
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)
    michelangelo.forward(random.randrange(1, 300))
    leonardo.forward(random.randrange(1, 300))

    #Test 2
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)
    max_distance = 30
    for i in range(10):
        michelangelo.forward(random.randrange(max_distance))
        leonardo.forward(random.randrange(max_distance))

    # Part B - complete part B here
    donatello = turtle.Turtle()
    for i in [3,4,6,8,20,100]:
        for j in range(i):
            donatello.forward(10)
            donatello.left(360/i)
        donatello.clear()


    window.exitonclick()
main()
