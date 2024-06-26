from window import Window
from purpleRain import PurpleRain
from fireWork import Rocket

if __name__ == "__main__":
    window = Window(800, 600)
    lightblue = (135, 160, 250)
    window.add_mode(PurpleRain(window.screen, 10, 1, (128, 0, 128), (0,0,0)))
    window.add_mode(Rocket(window.screen, 10, 10))
    window.run()
