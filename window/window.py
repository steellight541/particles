import pygame

class Window:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.modes = { }
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Modes Menu")
        self.clock = pygame.time.Clock()
        self.mode = None
        self.selected_mode = 0
    
    def add_mode(self, mode: object):
        self.modes[mode.__class__.__name__] = mode

    def draw_display(self):
        font = pygame.font.Font(None, 36)
        for i, mode in enumerate(self.modes):
            text = font.render(mode, True, (255, 255, 255))
            self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2 + i * 50))
        text = font.render("Selected: " + list(self.modes.keys())[self.selected_mode], True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2 + len(self.modes) * 50))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                self.key_down(event.key)

    def key_down(self, key):
        match key:
            case pygame.K_UP:
                self.selected_mode = (self.selected_mode - 1) % len(self.modes)
            case pygame.K_DOWN:
                self.selected_mode = (self.selected_mode + 1) % len(self.modes)
            case pygame.K_RETURN:
                self.mode = list(self.modes.keys())[self.selected_mode]
                pygame.display.set_caption(self.mode)
            case pygame.K_BACKSPACE:
                self.modes[list(self.modes.keys())[self.selected_mode]].reset()
                self.mode = None
                pygame.display.set_caption("Modes Menu")

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.mode == None:self.draw_display()
        else: self.modes[list(self.modes.keys())[self.selected_mode]].draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.events()
            self.draw()
            self.clock.tick(60)
