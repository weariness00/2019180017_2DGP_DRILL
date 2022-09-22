from pico2d import *
import math

open_canvas(800,600)

player = load_image("Lecture04_2D_Rendering/character.png")
grass = load_image('Lecture04_2D_Rendering/grass.png')

math.sin(270/360 * 2 *math.pi)

x = 400; y = 90

def MoveRectangle():
    global x; global y
    while x < 800 - 20:
        x = x + 10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)
        pass  
    while y < 600 - 40:
        y = y + 10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)
        pass;
    while x > 0 + 20:
        x = x - 10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)
        pass;
    while y > 0 + 90:
        y = y - 10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)
        pass;
    while x != 400:
        x = x + 10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)
        pass;       
    pass

def MoveCircle():
    global x; global y

    while True:
        tan = math.atan((x - 400)/(y - 300))
        sin = x + math.sin(tan)
        cos = y + math.cos(tan)
        x = x + sin*10
        y = y + cos*10
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(x,y)
        delay(0.01)

        if x == 400 and y == 90:
            break;
        pass
    pass

while True:
    MoveRectangle()
    MoveCircle()
    pass