from src.core.camera import camera

effects = []


class Effect:
    def __init__(self, x, y, xspeed, yspeed, life, image):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.life = life
        self.image = image
        global effects
        effects.append(self)

    def draw(self, screen):
        self.life -= 1
        self.x += self.xspeed
        self.y += self.yspeed
        if self.life <= 0:
            global effects
            effects.remove(self)
        screen.blit(self.image, (self.x + 7 - camera.x, self.y - 10 - camera.y))
