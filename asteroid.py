import pygame 
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            #splits asteroid into two smaller ones
            random_angle = random.uniform(20, 50)
            velocity = self.velocity.rotate(random_angle)
            asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
            asteroid.velocity = velocity
            asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
            asteroid.velocity = self.velocity.rotate(-random_angle)