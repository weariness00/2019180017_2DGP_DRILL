from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
running = True
left, right, up, down = False, False, False, False
dirX, dirY = 0, KPU_HEIGHT - 30
frame = 0

idle_state = 0

def Move():
    global x, y
    global running
    global dirX, dirY
    global frame
    global idle_state
    if left:
        dirX = -1
        idle_state = 0
    elif right:
        dirX = 1
        idle_state = 1
    else:
        if idle_state == 0:
            idle_state = 2
        elif idle_state == 1:
            idle_state = 3
        dirX = 0
    if up:
        dirY = 1
        if idle_state == 2:
            idle_state = 0
        elif idle_state == 3:
            idle_state = 1
    elif down:
        if idle_state == 2:
            idle_state = 0
        elif idle_state == 3:
            idle_state = 1
        dirY = -1
    else:
        dirY = 0

    x += dirX * 5
    y += dirY * 5
    if x < 20 or x > KPU_WIDTH - 20:
        x -= dirX * 5
    if y < 30 or y > KPU_HEIGHT - 30:
        y -= dirY * 5

    character.clip_draw(frame * 100, 100 * idle_state, 100, 100, x, y)

    update_canvas()
    pass

def handle_events():
    global running, left, right, up, down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                right = True
            elif event.key == SDLK_LEFT:
                left = True
            elif event.key == SDLK_UP:
                up = True
            elif event.key == SDLK_DOWN:
                down = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right = False
            elif event.key == SDLK_LEFT:
                left = False
            elif event.key == SDLK_UP:
                up = False
            elif event.key == SDLK_DOWN:
                down = False
    pass


open_canvas(KPU_WIDTH,KPU_HEIGHT)
character = load_image('animation_sheet.png')
tuk = load_image('TUK_GROUND.png')
while running:
    clear_canvas()
    tuk.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    handle_events()
    frame = (frame + 1) % 8
    Move()
    delay(0.02)