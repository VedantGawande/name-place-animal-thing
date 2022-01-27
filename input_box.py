import pygame

class Box():
    def __init__(self,screen,coordinates,width,height,max_width,size,user_input):
        super().__init__()
        self.user_input = user_input
        self.screen = screen
        self.x, self.y = coordinates
        self.width = width
        self.height = height
        self.max_width = max_width
        self.color_a = pygame.Color('lightskyblue3')
        self.color_p = pygame.Color('gray15')
        # self.color_a = pygame.Color('#D1E231')
        # self.color_p = pygame.Color('lavender')
        self.color = self.color_p
        self.size = size
        self.bottom = 0
        self.active_status = False
    def create_box(self):
        self.box_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.bottom = self.box_rect.bottom

    def draw1(self):
        pygame.draw.rect(self.screen,self.color,self.box_rect,self.size)


    def update(self):
        self.box_rect.w = 100
        self.bottom = self.box_rect.bottom
        self.box_rect.width = self.width