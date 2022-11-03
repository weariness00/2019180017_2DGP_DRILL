from pico2d import *
import game_framework
import Game_World

from grass import Grass
from boy import Boy


boy = None
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass

    boy = Boy()

    Game_World.World_Init(5)

    Game_World.Add_Object(Grass(), 0)
    Game_World.Add_Object(boy, 1)
    Game_World.Add_Object(Grass(y= 10), 2)

# 종료
def exit():
    Game_World.clear()

def update():
    for obj in Game_World.All_Objcet():
        obj.update()



def draw_world():
    for obj in Game_World.All_Objcet():
        obj.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
