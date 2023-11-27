class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (85, 195, 247)
        # Ship settings
        self.ship_speed_factor = 0.255
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 6
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.055
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale