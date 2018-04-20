Day 1 - [Here](https://rameshbalan.github.io/Python-Course/Day1) 
Day 2 - [Here](https://rameshbalan.github.io/Python-Course/Day2) 
Day 3 - [Here](https://rameshbalan.github.io/Python-Course/Day3)
Day 4 - [Here](https://rameshbalan.github.io/Python-Course/Day4)
Day 5 - [Here](https://rameshbalan.github.io/Python-Course/Day5)
Day 6 - [Here](https://rameshbalan.github.io/Python-Course/Day6)
Day 7 - [Here](https://rameshbalan.github.io/Python-Course/Day7)
Day 8 - [Here](https://rameshbalan.github.io/Python-Course/Day8)

## Ta - Daaaa
### Surprise Surprise !!!
#### The following is a short quiz just to refresh on various concepts learnt so far. 

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSe9tWl31yhsJKICsMF7AWSH_-jMLOuY5NArAaT7va9tCfckZQ/viewform?embedded=true" width="1020" height="760" frameborder="0" marginheight="0" marginwidth="200">Loading...</iframe>


## Introduction to Python Graphics using Turtle

“Turtle” is a python feature like a drawing board, which lets you command a turtle to draw all over it!
You can install it using the following command `sudo apt-get install python3-tk`.

You can use functions like turtle.forward(...) and turtle.left(...) which can move the turtle around.

Here are some of the commands that you can use:

| Turtle Function  | Description  |
| ------------- | ------------- |
|  turtle.left(x) | turns left by x pixels |
| turtle.right(x)  | turns right by x pixels  |
|  turtle.forward(x) | moves forward by x pixels |
| turtle.backward(x)  | moves backward by x pixels  |
|  turtle.goto(x,y) | repositions to the location `x,y` in the drawing board |
| turtle.color("color")  | changes the color from black to "color"  |

Remember `x` is a integer/float value in pixels.  

Before you can use turtle, you have to import it.

<iframe src="https://trinket.io/embed/python/68027d8ebb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Play around and learn more :smile:.

Copy paste the following code snippet to the trinklet window and see what happens.

```python
import turtle 

pattern = turtle.Turtle()

pattern.pencolor("blue")

for i in range(50):
    pattern.forward(50)
    pattern.left(123) # Let's go counterclockwise this time 
    
pattern.pencolor("red")
for i in range(50):
    pattern.forward(100)
    pattern.left(123)
    
turtle.done()
```

### Challenge:

a. Create a beautiful abstract pattern. Use for loops and/or while loops as necessary.  
(or)  
b. Animate a biological concept of your choice.  
