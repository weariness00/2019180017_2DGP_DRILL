from pico2d import *
import game_framework
import play_state

# fill here
image = None

def enter():
    # fill here
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():
    # fill here
    pass

def draw():
    # fill here
    clear_canvas()
    play_state.draw_World()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_b:
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.boy.append(play_state.Boy())
                case pico2d.SDLK_KP_MINUS:
                    if len(play_state.boy) is not 1:
                        del play_state.boy[-1]

def pause():
    pass

def resume():
    pass
