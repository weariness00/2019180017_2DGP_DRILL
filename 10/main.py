from pico2d import *
import play_state
import logo_state

states = (logo_state, play_state)

open_canvas()
for state in states:
    state.Enter()  # 초기화
    while state.running:  # 게임 루프
        state.handle_events()

        state.Update()
        state.Draw()
        pass
    state.Exit()  # 종료
    pass
close_canvas()
