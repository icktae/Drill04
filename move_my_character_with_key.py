from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sonic_animation.png')

# 캐릭터 이동 함수
def handle_events():
    global running
    global x
    global y
    global dir_lr
    global dir_ud

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            # 오른쪽 이동
            if event.key == SDLK_RIGHT:
                dir_lr += 1

            # 왼쪽 이동
            elif event.key == SDLK_LEFT:
                dir_lr -= 1

            # 위쪽 이동
            elif event.key == SDLK_UP:
                dir_ud += 1

            # 아래쪽 이동
            elif event.key == SDLK_DOWN:
                dir_ud -= 1

            # esc 탈출
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_lr -= 1
            elif event.key == SDLK_LEFT:
                dir_lr += 1

            elif event.key == SDLK_UP:
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                dir_ud += 1

# 캐릭터의 형상 변환 함수
def character_image(z) :
    character.clip_draw(frame * 100, z, 100, 100, x, y)

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
dir_lr = 0
dir_ud = 0

dir_move = 'right'
character_move = False

while running :
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 경계 구간 멈춤
    stop_x = x + dir_lr * 20
    stop_y = y + dir_ud * 20

    if 20 <= stop_x <= 1270 and 40 <= stop_y <= 1010:
        x = stop_x
        y = stop_y

    if dir_lr > 0:
        dir_move = 'right'
    elif dir_lr < 0:
        dir_move = 'left'

    # 움직임 여부 체크
    character_move = (dir_lr != 0 or dir_ud != 0)

    if character_move:
        if dir_move == 'right':
            character_image(100)
        elif dir_move == 'left':
            character_image(10)

    else:
        if dir_move == 'right':
            character_image(300)
        elif dir_move == 'left':
            character_image(200)


    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    delay(0.05)


close_canvas()


