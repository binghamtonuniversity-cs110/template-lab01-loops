
def main():
    #Part A
    window = turtle.Screen()       # 2.  Create a screen
    window.bgcolor('lightblue')

    michelangelo = turtle.Turtle()    # 3.  Create two turtles
    leonardo = turtle.Turtle()
    michelangelo.color('orange')
    leonardo.color('blue')
    michelangelo.shape('turtle')
    leonardo.shape('turtle')


    michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
    leonardo.up()
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)


    # 5. your code goes here


    # Part B - complete part B here


    window.exitonclick()
main()
