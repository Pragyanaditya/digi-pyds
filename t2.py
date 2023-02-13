from turtle import * # import turtle module

speed('fastest')
pencolor('red')
pensize(3)
fillcolor('blue')
for i in range(10,0,-2):
    begin_fill()
    circle(i*10)
    
    lt(25)
    end_fill()

hideturtle()
mainloop()