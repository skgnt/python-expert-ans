class character:
    def __init__(self, work, points, mp):
        self.work = work
        self.points = points
        self.mp = mp

    def info(self):
        print(self.work)
        print(self.points)
        print(self.mp)


human1 = character("主人公", 150, 30)
human1.info()

human2 = character("魔法つかい", 80, 30)
human2.info()

human3 = character("賢者", 70, 30)
human3.info()
