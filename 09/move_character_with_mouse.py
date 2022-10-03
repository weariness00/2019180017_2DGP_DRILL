from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1000, 800

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE or event.key == SDLK_q:
                running = False
    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)

# fill here
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True

sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = sx, sy
ax, ay = x, y
t = 0
frame = 0

left = 0
right = 1
idle = right

def reset_world():
    global sx, sy
    global ax, ay
    global t
    global idle

    ax, ay = randint(0, TUK_WIDTH), randint(0, TUK_HEIGHT)
    t = 0
    sx, sy = x, y

    if sx > ax:
        idle = left

    if sx < ax:
        idle = right

    pass

def update_world():
    global x, y
    global t

    t += 0.0025

    x = (1 - t) * sx + t * ax
    y = (1 - t) * sy + t * ay

    if t >= 1.0:
        reset_world()

    pass

reset_world()

while running:
    update_world()

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2, 1000, 800)

    arrow.draw(ax, ay)
    character.clip_draw(frame * 100, 100 * idle, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()


