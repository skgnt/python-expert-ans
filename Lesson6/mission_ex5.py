import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

# 弾のクラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        
        if 600>y:
            y=600
        
        self.rect = pygame.Rect(x-5, y-5, 10, 30) # 弾の矩形領域を設定
        self.speed = 6 # 弾の速度を設定

    def update(self):
        self.rect.move_ip(0, -self.speed) # 弾を上に移動させる
        self.check_off_screen()

    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill()

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect) # 弾の描写

# 敵のクラス
class Enemy(pygame.sprite.Sprite):
    finish=False
    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 赤い四角形を描画
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.target_position=random.randint(1,589)
    def update(self):
        self.rect.y += 2  # 下に移動する
        if self.rect.x<self.target_position:
            self.rect.x+=2
        elif self.rect.x > self.target_position:
            self.rect.x-=2
            self.rect.x-=2
        
        if abs(self.rect.x-self.target_position)<=2:
            self.target_position=random.randint(1,589)
        self.check_off_screen()

    def check_off_screen(self):
        if self.rect.top > 700:
            self.kill()
            Enemy.finish=True

# ゲームクラス
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 700)) # 画面の大きさ
        self.bullets = [] # 弾のオブジェクト用リスト
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 55)
        self.score=0

    def run(self):
        clock = pygame.time.Clock()
        time=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if pygame.mouse.get_pressed()[0]: # 左クリックされたら
                n_time=pygame.time.get_ticks()
                if abs(time-n_time)>500:
                    x, y = pygame.mouse.get_pos()
                    bullet = Bullet(self.bullet_group, x, y)
                    self.bullets.append(bullet)
                    time=n_time


            for bullet in self.bullets:
                bullet.update()

            # 敵を追加
            if random.randint(1, 100) < 2: # 2%の確率で敵を追加
                x = random.randint(50, 590) # 画面内のランダムな位置に敵を配置
                enemy = Enemy(self.enemy_group, x, 0)

            self.screen.fill("YELLOW") # 画面に黒を表示

            for bullet in self.bullets:
                bullet.draw(self.screen)

            self.enemy_group.update()
            self.enemy_group.draw(self.screen)
            if Enemy.finish:
                break

            # 衝突検出
            collisions = pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, False, True)
            self.score+=len(collisions)
            text = self.font.render(f'{self.score}', True, (0, 0, 0))   # 表示する文字列を作る
            self.screen.blit(text, [0, 0])

            pygame.display.flip()

            clock.tick(FPS)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            text = self.font.render('GAME FINISH', True, (0, 0, 0))   # 表示する文字列を作る
            self.screen.blit(text, [200, 350])
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()