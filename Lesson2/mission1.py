import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
# 弾のクラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.rect = pygame.Rect(x-5, y-5, 30, 30)
        self.speed = 8
    def update(self):
        self.rect.move_ip(0, -self.speed)
        self.check_off_screen()
    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill()
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500  )) 
        self.bulltes = [] 
        self.bullet_group = pygame.sprite.Group()
    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            if pygame.mouse.get_pressed()[0]: 
                x, y =pygame.mouse.get_pos()

                bullet =Bullet(self.bullet_group, x, y)
                self.bulltes.append(bullet)
            
            for bullet in self.bulltes:
                bullet.update()
                self.screen.fill(BLACK)
            for bullet in self.bulltes:
                bullet.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()