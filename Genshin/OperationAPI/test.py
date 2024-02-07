import pygame
from dependent import *

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# 初始化变量，用于保存前一次位置
previous_x = 0
previous_y = 0

# 初始化监听器
listener = Listener()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取鼠标相对移动量
    delta_x, delta_y = pygame.mouse.get_rel()

    # 更新前一次位置
    previous_x += delta_x
    previous_y += delta_y

    # 调用监听器的鼠标移动处理函数，在此记录鼠标移动事件
    listener.on_move(previous_x, previous_y)

    pygame.display.flip()

# 退出Pygame
pygame.quit()
