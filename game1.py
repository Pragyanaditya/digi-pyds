import pgzrun

#music.play('r') #bgm music



b = Rect((50,50), (100,50))
vx, vy =3,5 #global variable

def draw():
    screen.fill('red')
    screen.draw.filled_rect(b,'blue')

def update():
    global vx
    global vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left <0:
        vx=-vx
        sounds.s1.play()
    if b.bottom > 600 or b.top<0:
        vy =-vy
pgzrun.go()