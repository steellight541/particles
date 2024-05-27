from pygame.draw import line
from random import randint

class Drop:
    # a rain drop
    def __init__(self,screen, color, wind_intensity, rain_intensity, lenght) -> None:
        self.screen = screen
        self.color = color
        self.wind_intensity = wind_intensity
        self.rain_intensity = rain_intensity
        self.length = lenght
        self.x = randint(0, self.screen.get_width())
        self.y = randint(-self.screen.get_height(), 0)
        self.falling = True
        
    def fall(self) -> None:
        # update x, y depending on the wind intensity and the rain intensity make it drop more seamlessly
        self.y += 10 * self.rain_intensity
        self.x += self.wind_intensity
        if self.y > self.screen.get_height():
            self.falling = False

    def draw(self) -> None:
        # tilt the line to make it correspond to the wind intensity
        line(self.screen, self.color, (self.x, self.y), (self.x + self.wind_intensity, self.y + self.length), 2)
        self.fall()

