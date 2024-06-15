class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed = 1.5
        self.ship_limit = 0

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # 外星人设置
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动，为-1 表示向左移动
        self.fleet_direction = 1
