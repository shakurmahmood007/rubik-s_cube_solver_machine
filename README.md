# rubik-s_cube_solver_machine
My facebook ID for any query- https://www.facebook.com/100085364779674

3x3x3 Rubik's Cube solving with a new technique and building a solver machine with 5 stepper motors.

Here, in Presentation_on.pdf I have discussed the total project in brief.

And, in Project_book.pdf I have described the total project in detail.

Project.py is the code if you want to run it without machine implementation. It runs on python2.

nema23.py is the code for implementing using a raspberry pi, 5 stepper motors and 5 drv8825 drivers. It runs on python3.

example.py is the code for testing a single stepper motor. It runs on python3.

#-----------------------------------------------------

For fiving input, imagine the rubiks cube as letter 'T', then give inputs but each input will be only a letter for each color (like g gor green, r for red). And must use 6 different letters for 6 different colors. After inputting each letter press enter and must input lower case letters. Now, Imagine the rubik's cube like this-

---
 |
 |
 |

So, 6 sides are-

1-2-3-
  4|
  5|
  6|

Here, 2 is the top side of the rubik's cube and 5 is the bottom side. 4 is the side infront of you and 6 is the side just opposite of you. 1 is the left side and 3 is the right side.

So, after putting a rubik's cube infront of you, watch it from the top, then start inputting from the left side (so, start from 1). And for each side start inputting from the top left corner.

---
---
---

So, 9 boxes of each side are-

1-2-3-
4-5-6-
7-8-9-

So, start inputting from 1.

So, there are need to 54 inputs and input one after another. So, inputting the letter for the color of the box 9 of side 1 snd pressing enter, start inputting the letter for the color of the box 1 of side 2 (and ofcourse press enter). 

Not to do any mistake I at first write the letters in a notepad and then copied-pasted and pressed enter. Example of the input-
b
o
r
w
r
b
b
w
y
g
y
b
r
w
y
o
y
r
r
r
g
o
o
b
g
o
o
g
g
w
o
b
b
o
y
w
y
r
b
g
y
w
r
g
w
w
r
o
g
g
w
y
b
y
