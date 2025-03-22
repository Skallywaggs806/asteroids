import pygame
import sys

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():

    with open("highscore.txt", "r") as file:
        HIGH_SCORE = int(file.read())

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    score = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over! Score: {score}")
                if score > HIGH_SCORE:
                    print(f"New high score: {score}")
                    with open('highscore.txt', 'w') as file:
                        file.write(f"{score}")
                else:
                    print(f"High score: {HIGH_SCORE}")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        

        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")







if __name__ == "__main__":
    main()