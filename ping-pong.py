from pygame import *


finish = False

window_height = 700
window_width = 500

window = display.set_mode((window_height,window_width))  #оформление
display.set_caption("Пинг-понг")
background = transform.scale(image.load('Задний фон.jpg'), (window_height, window_width))


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

player1 = Player(40, 390, 5, 'ракетка для пинг понга.jpg', 65,65 )

player2 = Player(40, 40, 5, 'ракетка для пинг понга.jpg', 65,65 )

game = True   #игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:

        window.blit(background, (0, 0))
        player1.paint()
        player2.paint()
        display.update()