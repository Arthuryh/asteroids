import pygame
import circleshape

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update(self, dt):
        self.position += (self.velocity * dt)