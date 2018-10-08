mport turtle
import time


turtle.setup(width=0.8, height=0.5)
turtle.bgcolor("red")           
turtle.fillcolor("yellow")      
turtle.color('yellow')         
turtle.speed(15)                


turtle.begin_fill()     
turtle.up()
turtle.goto(-500, 110)  
turtle.down()
for i in range(5):
    turtle.forward(150) 
    turtle.right(144)    
turtle.end_fill()       
time.sleep(1)

turtle.begin_fill()
turtle.up()
turtle.goto(-300, 195)
turtle.setheading(305)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)     
turtle.end_fill()
time.sleep(1)


turtle.begin_fill()
turtle.up()
turtle.goto(-250, 112)
turtle.setheading(30)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

turtle.begin_fill()
turtle.up()
turtle.goto(-250, 45)
turtle.setheading(5)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

turtle.begin_fill()
turtle.up()
turtle.goto(-300,-10)
turtle.setheading(300)
turtle.down()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()
time.sleep(3)
