#### CS 110 - Fall 2018
# Lab 3 - Turtle Racing Lab
## Due Date: 5:00, September 13th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab3.py

### Grading Rubric

**_TOTAL: 16 points_**
* **Part A: 5 points**
   * Race 1 consists of a single call for each turtle using a random value between 1 and 100 (1 point)
   * Race 2 uses iteration to advance each turtle 10 times (1 point)
   * Each race 2 loop iteration advances both turtles by separate random values (1 point)
   * Turtle positions are reset after each race (2 points)
* **Part B: 10 points**
   * Turtle correctly draws each shape (2 points)
   * Turtle clears each shape before drawing the next (3 points)
   * Turtle uses a for loop and calculated angles to draw the shapes (5 points)
* **Part C: 1 point**
    * Follows requested project structure and submission format
    * Enclosed in a main. Only the call to main and imports are in global space. (2 points)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:

* Use python data
* Use python modules

| | Meaning |
|:----:|---------|
| :bulb: | Tips and useful information |
| :warning: | Caution! This could cause you problems. |
| :no_entry_sign: | Danger! Don't do this! |

## Part A: Random Numbers
Before we begin writing code for this lab, we need to introduce one more Python module. The `random` module allows us to generate random numbers. It’s easy to use:

```python
import random
def main():
    x = random.randrange(1,10)
    print(x)
main()
```
The `randrange` function as called in the example above, generates a random number from 1 to 9. Even though we said 10 the `randrange` function goes up to, but does not include, the upper limit value. Now if you run the program over and over again you should see that each time you run it a different number is generated. Random numbers are the basis of all kinds of interesting programs we can write, and the `randrange` function is just one of many functions available in the `random` module.

### Turtle Races
In this lab we are going to work step by step through the problem of racing turtles. The idea is that we want to create two or more turtles and have them race across the screen from left to right. The turtle that goes the farthest is the winner.

There are several different, and equally plausible, solutions to this problem. Let’s look at what needs to be done, and then look at some of the options for the solution.

To start, let’s think about a solution to the simplest form of the problem, a race between two turtles. We’ll look at more complex races later. When you are faced with a problem like this in computer science it is often a good idea to find a solution to a simple problem first and then figure out how to make the solution more general.
Here is a possible sequence of steps that we will need to accomplish:
1. Import the modules we need
2. Create a screen
3. Create two turtles
4. Move the turtles to their starting positions
5. Send them moving across the screen

The python code provided in the repository contains the Python code for the first 4 steps above.

:bulb: You can review the documentation for the turtle library, with its list of methods, [here](https://docs.python.org/3.3/library/turtle.html?highlight=turtle).

Now, you have a couple possibilities for how to fill in code for step 5. Try coding each of the following to see the different kinds of behavior.
1. Use a single call to `forward` for each turtle, using a random number between 1-100 as the distance to move.
   * Reset the turtles to their starting position [(-100, 20), (-100, -20) respectively] once you are done.
2. Make 10 calls to forward alternating on each turtle with the random range between 0 and 10.
   * A new random value should be generated again for each separate call to forward.
   * Reset the turtles to their respective starting positions once you are done with the loop.

So, which of these programs is better? Which of these programs is most correct? These are excellent questions. Method 1 is certainly the simplest, but it isn’t very satisfying as far as a race is concerned. Each turtle simply moves their distance on their turn. Method 2 is probably the most ‘realistic’ assuming realism is very important when we’re talking about a simulated race of virtual turtles.

__Show the CA your code.__

__--END OF IN LAB REQUIRED WORK--__

_You may continue to work on the remainder of the lab on your own time or in lab_

## Part B: Modules
Write additional code _in the main_ to have your turtle draw these regular polygons (regular means all sides the same lengths, all angles the same). Note that you will need to calculate the angles based on the number of sides, not by hardcoding it. Since the angles of every regular polygon adds up to 360 degrees, you can determine the angles by dividing the number of sides by 360 degrees. Using a turtle, draw the following:

* equilateral triangle
* square
* octagon (8 sides)
* icosagon (20 sides)
* hectogon (100 sides)

You must clear the previous shape before drawing the next shape. The turtle library has a method that allows you to do this.

## Part C : Code Organization and Submission
* Required code organization:
   * lab3.py

Below is just a reminder of the commands you should use to submit your code. If you cannot remember the exact process, please review Lab 1.

*These commands all presume that your current working directory is within the directory tracked by `git`.*

You will need to do the following when your submission is ready for grading.

```shell
git commit -a -m "final commit"
git push
```

To complete your submission, you must copy and paste the commit hash into MyCourses. Go to MyCourses, select CS110, and then assignments. Select Lab 3, and where it says text submission, paste your commit hash. You can get your latest commit hash with the following command:

```shell
git rev-parse HEAD
```    

:warning: Remember, you __MUST__ make a submission on mycourses before the deadline to be considered on time.
