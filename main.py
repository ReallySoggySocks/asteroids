import pygame
import sys
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)

        for obj in asteroids:
            if player.collision(obj) == True:
                sys.exit("Game over!")

        for obj in asteroids:
            for bullet in shots:
                if bullet.collision(obj) == True:
                    bullet.kill()
                    obj.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()