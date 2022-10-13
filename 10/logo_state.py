from pico2d import *
import game_framework
import title_state

# fill here
image = None
logo_time = 0.0

def enter():
    # fill here
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():
    # fill here
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
        pass
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    # fill here
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





