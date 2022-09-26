from pico2d import *

window_W, window_H = 800, 600

open_canvas(window_W, window_H)

player = load_image("Player.png")

x, y = 0, 0

def SmallPlayer_Move():
    global x, y
    frame = 0
    for i in range(0, 8 * 2):
        clear_canvas()
        player.clip_draw(frame * 51 , 450 - 43, 46, 43, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.15)
        get_events()
        pass
    pass

def Player_Work():
    global x, y
    frame = 0
    for i in range(0, 8 * 2):
        clear_canvas()
        player.clip_draw(frame * 59, 0, 60, 90, x, y)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.15)
        get_events()
        pass
    pass

def Player_Fire():
    global x, y
    frame = 0
    for i in range(0, 9):
        clear_canvas()
        player.clip_draw(frame * 57, 110, 60, 90, x, y)
        update_canvas()
        frame = (frame + 1) % 9
        delay(0.15)
        get_events()
        pass
    for i in range(0, 3):
        clear_canvas()
        player.clip_draw(8 + (frame + 5) * 104, 110, 104, 130, x, y + 30)
        update_canvas()
        frame = (frame + 1) % 3
        delay(0.15)
        get_events()
        pass
    frame = 2
    for i in range(0, 3):
        clear_canvas()
        player.clip_draw(8 + (frame + 5) * 104, 110, 104, 130, x, y + 30)
        update_canvas()
        frame = (frame - 1)
        delay(0.15)
        get_events()
        pass
    frame = 8
    for i in range(0, 9):
        clear_canvas()
        player.clip_draw(frame * 57, 110, 60, 90, x, y)
        update_canvas()
        frame = (frame - 1)
        delay(0.15)
        get_events()
        pass
    pass

x = window_W/2; y =window_H/2


i = 0
while i < 1:
    i += 1
    Player_Fire()
    Player_Work()
    SmallPlayer_Move()
    pass
