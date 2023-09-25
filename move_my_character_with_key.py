from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global x
    global y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            # 오른쪽 이동
            if event.key == SDLK_RIGHT:
                dir += 1
            # 왼쪽 이동
            elif event.key == SDLK_LEFT:
                dir -= 1
            # esc 탈출
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

running = True
x = 1280 // 2
frame = 0
dir = 0

while running :
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x ,90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 10
    delay(0.05)


close_canvas()


