import pygame
import circleshape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_value = random.uniform(20,50)
            random_value_neg = self.velocity.rotate(-random_value)
            random_value = self.velocity.rotate(random_value)

            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

            new_asteroid1.velocity = random_value * 1.2
            new_asteroid2.velocity = random_value_neg * 1.2
