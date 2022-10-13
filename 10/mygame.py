# fill here
from pico2d import *
import logo_state
import game_framework
import item_state
import play_state

open_canvas()
game_framework.run(play_state)
close_canvas()