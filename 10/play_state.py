from pico2d import *
import game_framework
import title_state
import item_state
import Setting_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1 #오른쪽
        self.image = load_image('animation_sheet.png')
        self.ball_Image = load_image('ball21x21.png')
        self.big_ball_Image = load_image('ball41x41.png')

        self.item = None

        self.__speed = 10

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * self.__speed

        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

        if self.item == 'Ball':
            self.ball_Image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Big_Ball':
            self.big_ball_Image.draw(self.x + 10, self.y + 50)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(Setting_state)


boy = []
grass = None

def enter():
    global boy, grass, running

    boy.append(Boy())
    grass = Grass()
    pass

# finalization code
def exit():
    global boy, grass

    del boy
    del grass

    pass

def update():
    global boy
    for obj in boy:
        obj.update()
    pass

def draw():
    global boy, grass
    clear_canvas()

    draw_World()

    update_canvas()

    delay(1/60)
    pass

def pause():
    pass

def resume():
    pass

def draw_World():
    grass.draw()
    for obj in boy:
        obj.draw()
    pass