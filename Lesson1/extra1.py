class character:
    def __init__(self, work, points, mp):
        self.work = work
        self.points = points
        self.mp = mp

    def info(self):
        print(self.work)
        print(self.points)
        print(self.mp)

    def hp_ope(self, ope):
        self.points += ope


human1 = character("主人公", 150, 30)
human1.info()

human1.hp_ope(100)

human1.info()
