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

    def atk(self, use_mp):
        self.mp -= use_mp
        return use_mp*10


human1 = character("ナイト", 100, 200)
mpatk = human1.atk(10)
human1.info()
print(mpatk)
