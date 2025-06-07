import pygame as pg

pg.init()

window = pg.display.set_mode((800, 600))
pg.display.set_caption("Ping Pong Game")

# First board
first_board_x = 10
first_board_y = 100
first_board_pos_x = 30
first_board_pos_y = 300
def FirstBoard():
    pg.draw.rect(window, (0, 0, 255), (first_board_pos_x, first_board_pos_y, first_board_x, first_board_y))

# Second board
second_board_x = 10
second_board_y = 100
second_board_pos_x = 760
second_board_pos_y = 300
def SecondBoard():
    pg.draw.rect(window, (255, 0, 0), (second_board_pos_x, second_board_pos_y, second_board_x, second_board_y))

# Ball
ball_x = 100
ball_y = 200
ball_speed_x = 0.2
ball_speed_y = 0.2
def ball():
    pg.draw.circle(window, (255, 255, 255), (ball_x, ball_y), 10)

def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x >= 800:
        ball_speed_x = -ball_speed_x 
    if ball_y <= 0 or ball_y >= 600:
        ball_speed_y = -ball_speed_y 

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    keys = pg.key.get_pressed()
    
    if keys[pg.K_w] and first_board_pos_y > 0:
        first_board_pos_y -= 0.3
    if keys[pg.K_s] and first_board_pos_y < 600 - first_board_y:
        first_board_pos_y += 0.3
    if keys[pg.K_UP] and second_board_pos_y > 0:
        second_board_pos_y -= 0.3
    if keys[pg.K_DOWN] and second_board_pos_y < 600 - second_board_y:
        second_board_pos_y += 0.3
    if keys[pg.K_r]:
        first_board_y += 0.1
    if keys[pg.K_t]:
        first_board_y -= 0.1
    if keys[pg.K_i]:
        second_board_y += 0.1
    if keys[pg.K_o]:
        second_board_y -= 0.1
    if keys[pg.K_b] and (ball_speed_x and ball_speed_y) < 1:
        ball_speed_x += 0.1
        ball_speed_y += 0.1
    if keys[pg.K_n] and (ball_speed_x and ball_speed_y) > 0.1:
        ball_speed_x -= 0.1
        ball_speed_y -= 0.1
    if keys[pg.K_SPACE]:
        ball_x = 400
        ball_y = 300
        ball_speed_x = 0.2
        ball_speed_y = 0.2

    if ball_x > first_board_pos_x and ball_x < first_board_pos_x + first_board_x and ball_y > first_board_pos_y and ball_y < first_board_pos_y + first_board_y:
        ball_speed_x = -ball_speed_x

    if ball_x > second_board_pos_x and ball_x < second_board_pos_x + second_board_x and ball_y > second_board_pos_y and ball_y < second_board_pos_y + second_board_y:
        ball_speed_x = -ball_speed_x
    
    if ball_x < 0 or ball_x > 800:
        if ball_x < 0:
            print("Red player wins")
        if ball_x > 800:
            print("Blue player wins")
        run = False

    move_ball()

    window.fill((0, 0, 0))

    FirstBoard()
    ball()
    SecondBoard()

    pg.display.update()

pg.quit()
