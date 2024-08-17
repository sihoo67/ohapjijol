import tkinter as tk
import pygame
import random

# 게임 실행 함수
def run_game():
    root.destroy()  # 메인 창을 닫음
    pygame.init()

    # 색상 설정
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # 디스플레이 크기 설정
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

# 도움말을 표시하는 함수
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("도움말")
    
    help_text = (
        "움직임: 화살표 키\n"
        "게임 다시 시작: C\n"
        "게임 종료: Q"
    )
    
    label = tk.Label(help_window, text=help_text, font=("Arial", 12))
    label.pack(pady=20, padx=20)
    
    close_button = tk.Button(help_window, text="닫기", command=help_window.destroy)
    close_button.pack(pady=10)

# 메인 창 생성
root = tk.Tk()
root.title("스네이크 게임")

# 타이틀 라벨
title_label = tk.Label(root, text="스네이크", font=("Arial", 24))
title_label.pack(pady=20)

# 시작 버튼
start_button = tk.Button(root, text="시작", font=("Arial", 18), command=run_game)
start_button.pack(pady=10)

# 도움말 버튼
help_button = tk.Button(root, text="도움말", font=("Arial", 18), command=show_help)
help_button.pack(pady=10)

# 메인 루프 시작
root.mainloop()
