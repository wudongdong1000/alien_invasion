import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    pygame.mixer.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,
    ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")
    #开始游戏的主循环
    while True:
        gf.update_screen(ai_settings,screen,stats,ship,sb,aliens,bullets,play_button)
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,sb,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,bullets,aliens)
            gf.update_aliens(ai_settings,stats,screen,ship,sb,aliens,bullets)
        
run_game()

