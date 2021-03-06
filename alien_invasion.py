import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_states import GameStats
from button import Button
from scoreboard import Scoreboard
# from alien import Alien

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((600,300))
    # bg_color=(100,120,100)
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button=Button(ai_settings,screen,"Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    bg_color=(230,230,230)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    # ship=Ship(screen)
    ship=Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets=Group()
    aliens=Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建一个外星人
    # alien=Alien(ai_settings,screen)

    # 开始游戏的主循环
    while True:

        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # # 每次循环都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()
        # gf.check_events()
        # gf.check_events(ship)
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)


        # bullets.update()
        #
        # # 删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom<=0:
        #         bullets.remove(bullet)
        # # print(len(bullets))
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,sb,stats,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            gf.update_screen(ai_settings,screen,stats,sb,
                             ship,aliens,bullets,play_button)
        # gf.update_screen(ai_settings, screen, ship, aliens,bullets)
        # gf.update_screen(ai_settings,screen,ship,bullets)
        # gf.update_screen(ai_settings,screen,ship)

run_game()