import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting postion."""
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Movement flag
        self.move_right = False
        self.move_left = False

    def update(self):
        """update the ship's postion based on the movement of the flag."""

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed

        if self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its currunt location."""
        self.screen.blit(self.image, self.rect)

