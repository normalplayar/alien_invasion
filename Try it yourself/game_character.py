import pygame

class Penguin():
        def __init__(self,screen):
            """Initialize the character and set its starting position."""
            self.screen = screen
            # Load the ship image and get its rect.
            self.image = pygame.image.load("images/penguin.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            # Start each new ship at the bottom center of the screen.
            self.rect.center = self.screen_rect.center

        def blitme(self):
            """Draw the character at its current location."""
            self.screen.blit(self.image, self.rect)

class Rocket():
    def __init__(self,screen):
        """Initialize the character and set its starting position."""
        self.screen = screen
        # Load the rocket image and get its rect.
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new rocket at the  center of the screen.
        self.rect.center = self.screen_rect.center
        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up= False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 0.255
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= 0.255
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= 0.255
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 0.255
        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
