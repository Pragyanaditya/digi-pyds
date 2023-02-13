from turtle import * # import turtle module

speed('fastest')
n=100
d=360/n
pencolor('red')
for i in range(n):
    forward(1)
    left(d)
    write(i)

hideturtle()
mainloop()