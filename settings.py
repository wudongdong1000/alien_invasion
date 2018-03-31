from pygame.mixer import Sound

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        #初始化游戏的静态设置
        #屏幕设置
        self.screen_width=1366
        self.screen_height=700
        self.bg_color=(230,230,230)
        #飞船设置
        self.ship_limit=1
        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10
        #以什么样的速度加快游戏节奏
        self.speedup_scale=1.1
        #得分提高速度
        self.score_sccale=1.5
        self.initialize_dynamic_settings()
        #声音设置
        self.sound_qs=Sound('audio/qs.wav')
        self.sound_bz=Sound('audio/bz.wav')
        
    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        #fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction=1
        #击落一个外星人得分
        self.alien_points=10

    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.fleet_drop_speed+=1

        self.alien_points=int(self.alien_points*self.score_sccale)



