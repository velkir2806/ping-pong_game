class GameSprite(sprite.Sprite):  #создание классов
    def __init__(self, x_cor, y_cor, player_speed, player_image, w, h ):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
    
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_W] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

    
        
    
    