from window import Window
from purpleRain import PurpleRain

if __name__ == "__main__":
    window = Window(800, 600)
    lightblue = (135, 160, 250)
    window.add_mode(PurpleRain(window.screen, 0, 1, (128, 0, 128), lightblue))
    window.run()
