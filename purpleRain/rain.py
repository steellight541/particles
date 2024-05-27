from purpleRain.drop import Drop


class PurpleRain:
    def __init__(self, screen, wind_intensity, rain_intensity, rain_color, background_color) -> None:
        # arguments
        self.screen = screen
        self.wind_intensity = wind_intensity
        self.rain_intensity = rain_intensity
        self.rain_color = rain_color
        self.background_color = background_color
        # drops
        self.drops = []

    def get_drops(self) -> None:
        # remove the drops that arent falling
        self.drops = [drop for drop in self.drops if drop.falling]
        for i in range(len(self.drops), int(self.screen.get_width() // 4 * self.rain_intensity)):
            self.drops.append(Drop(self.screen, self.rain_color, self.wind_intensity, self.rain_intensity, 10))

    def draw(self) -> None:
        self.screen.fill(self.background_color)
        self.get_drops()
        for drop in self.drops:
            drop.draw()

    def reset(self) -> None:
        self.drops = []
