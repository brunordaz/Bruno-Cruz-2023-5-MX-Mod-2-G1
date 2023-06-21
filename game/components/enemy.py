

class Enemy:
    X_POX_LIST = [100, 150, 200, 250, 300, 350, 400, 450]
    Y_POS = 20
    SPEED_Y =1
    LEFT = "left"
    RIGHT = "right"
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100



    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.random.choice(self.X_POX_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.is_alive = False

    def update(self):
        self.move()

    def draw(self,screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.SPEED.y
        if self.mov_x == self.LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_x
            if self.index > self.INTERVAL or self.rect.x >= SC:
                self.mov_X = self.RIGHT
                drlf.index = 0

        self.index += 1
