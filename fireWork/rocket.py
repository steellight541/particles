from pygame.draw import circle, line
import pygame   
import random
from random import randint


class Particle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(0, 5)
    
    # from the center of the explosion, the particles will move in a random direction
    def move(self):
        self.x += random.randint(-25, 25)
        self.y += random.randint(-25, 25)
        self.radius -= 0.1
    
    def draw(self):
        self.move()
        if self.radius > 0:
            circle(self.screen, self.color, (self.x, self.y), self.radius)

class Rocket:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.x = randint(0, self.screen.get_width())
        self.y = self.screen.get_height()
        self.max_height = random.randint(self.screen.get_height() // 2, self.screen.get_height()//2 + 100)
        self.isFlying = True
        self.exploded = False
        self.particules = []

    def draw(self):
        if not self.exploded:
            line(self.screen, (255, 255, 255), (self.x, self.y), (self.x, self.y - 10), 2)
        else:
            for particle in self.particules:
                particle.draw()
            self.check_particules()
            if not self.particules:
                self.reset()
        if self.isFlying:
            self.move_up()

        
    def check_particules(self):
        for particle in self.particules:
            if particle.radius <= 0:
                self.particules.remove(particle)

    def move_up(self):
        if self.y > self.max_height:
            self.y -= 5
        else:
            self.isFlying = False
            self.explode()
    
    def explode(self):
        for _ in range(100):
            self.particules.append(Particle(self.screen, self.x, self.y))
        self.exploded = True

