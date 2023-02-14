from turtle import *

speed("fastest")
pencolor('green')
for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        for i in range(6):
            fd(50)
            rt(72)
        lt(72)
    rt(60)
hideturtle()
mainloop()