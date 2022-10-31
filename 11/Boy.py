from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER , AUTO_AU, AUTO_AD = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,

    (SDL_KEYDOWN, SDLK_a): AUTO_AD,
    (SDL_KEYUP, SDLK_a): AUTO_AU
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.sleepTimer = 100

        self.q = []
        self.cur_state = SLEEP
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # 리스트에 무언가 들어있으면
            event = self.q.pop()    # 이벤트 확인
            self.cur_state.exit(self)   # 현재 이벤트 탈출
            self.cur_state = next_state[self.cur_state][event]  # 다음 이벤트 저장
            self.cur_state.enter(self, event)  # 다음 이벤트 호출
            pass


    def draw(self):
        self.cur_state.draw(self)



    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.Add_Q(key_event)


    def Add_Q(self, key_event):
        self.q.insert(0, key_event)
        pass

        # for event in self.events:
        #     if event.type == SDL_KEYDOWN:
        #         match event.key:
        #             case pico2d.SDLK_LEFT:
        #                 self.dir -= 1
        #             case pico2d.SDLK_RIGHT:
        #                 self.dir += 1
        #     elif event.type == SDL_KEYUP:
        #         match event.key:
        #             case pico2d.SDLK_LEFT:
        #                 self.dir += 1
        #                 self.face_dir = -1
        #             case pico2d.SDLK_RIGHT:
        #                 self.dir -= 1
        #                 self.face_dir = 1
    pass

# 스테이트 구현

class IDLE:

    @staticmethod
    def enter(self, event):
        print('enter idle')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('exit idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

        self.sleepTimer -= 1
        if self.sleepTimer == 0:
            self.Add_Q(TIMER)
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

    pass

class RUN:
    @staticmethod
    def enter(self, event):
        print('enter run')
        if event == RD:
            self.dir = 1
        elif event == LD:
            self.dir = -1
        elif event == RU:
            self.dir = -1
        elif event == LU:
            self.dir = 1
        pass

    @staticmethod
    def exit(self):
        print('exit run')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass
    pass

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('enter sleep')
        self.dir = 0
        self.sleepTimer = 100
        pass

    @staticmethod
    def exit(self):
        print('exit sleep')
        pass

    @staticmethod
    def do(self):

        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           math.radians(90), 'None',
                                           self.x - 25, self.y- 40,
                                           100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           math.radians(-90), 'None',
                                           self.x + 25, self.y - 40,
                                           100, 100)
        pass

    pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('enter AUTO_RUN')
        self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self):
        print('exit AUTO_RUN')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        if self.x >= 800 or self.x <= 0:
            self.dir = -self.dir

        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 30, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 30, 200, 200)
        pass
    pass

next_state = {
    IDLE : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO_AD: AUTO_RUN, AUTO_AU: IDLE},
    RUN : {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, TIMER: RUN, AUTO_AD: AUTO_RUN, AUTO_AU: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO_AD: AUTO_RUN, AUTO_AU: IDLE},
    AUTO_RUN : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO_AD: IDLE, AUTO_AU: AUTO_RUN}
}