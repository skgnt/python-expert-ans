import pygame
#弾の色の設定
WHITE = (255, 255, 255)
#バックグラウンドの色の設定
BLACK = (0, 0, 0)
FPS = 60
# 弾のクラス
#Spriteクラスの継承
#Spriteクラスは特定の画像を表示するための規定クラス(親クラス)
class Bullet(pygame.sprite.Sprite):
    #コンストラクタ(初期化)
    def __init__(self, groups, x, y):
        """
        オーバーライド
        今回の場合はpygame.sprite.Spriteクラスの
        スプライトグループ設定を残したまま、
        座標設定、スピードの初期化を追加する
        """
        super().__init__(groups)
        #位置と大きさの設定
        self.rect = pygame.Rect(x-5, y-5, 30, 30)
        self.speed = 8
    
    #位置の更新
    def update(self):
        """
        move_ipは自分自身の移動を行うメソッドだが、
        あくまでテレポートさせるだけなので注意
        move_ip(x軸,y軸)
        """
        self.rect.move_ip(0, -self.speed)
        self.check_off_screen()
    def check_off_screen(self):
        #現在の下からの座標のメンバー変数
        if self.rect.bottom < 0:
            #全てのグループから自分自身を削除
            self.kill()
    def draw(self, surface):
        #四角を描写する
        #pygame.draw.rect(Surface, color, Rect, width=0)
        pygame.draw.rect(surface, WHITE, self.rect)

        
class Game():
    def __init__(self):
        #pygame自体の初期化
        pygame.init()
        #描画用ウィンドウの初期化
        self.screen = pygame.display.set_mode(( 700, 500  )) 
        #弾管理用配列の初期化
        self.bulltes = []
        #弾のグループを定義
        self.bullet_group = pygame.sprite.Group()
    def run(self):
        clock = pygame.time.Clock()
        while True:
            #イベントの取得
            for event in pygame.event.get():
                #終了ボタンの検知
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            #左クリック検知
            if pygame.mouse.get_pressed()[0]: 
                #マウス位置取得
                x, y =pygame.mouse.get_pos()
                #弾のインスタンス生成
                bullet =Bullet(self.bullet_group, x, y)
                #弾の配列に追加
                self.bulltes.append(bullet)
            
            
            for bullet in self.bulltes:
                #ウィンドウの初期化
                self.screen.fill(BLACK)
                #弾の移動メソッドの呼び出し
                bullet.update()
            for bullet in self.bulltes:
                bullet.draw(self.screen)
            #描画する
            pygame.display.flip()
            clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()
