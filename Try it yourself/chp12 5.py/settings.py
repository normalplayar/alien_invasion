class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 755
        self.screen_height = 600
        self.bg_color = (85, 195, 247)
        # Ship settings
        self.ship_speed_factor = 0.255
        # Bullet settings
        self.bullet_speed_factor = 0.2
        self.bullet_width = 10
        self.bullet_height = 2
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5