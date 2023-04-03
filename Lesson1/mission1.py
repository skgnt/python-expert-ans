class character:
    def __init__(self, work, points):
        self.work = work
        self.points = points

    def info(self):
        print(self.work)
        print(self.points)


print("名前:MP(マジックポイント)")
human1 = character("主人公", 20)
human1.info()

human2 = character("魔法つかい", 30)
human2.info()
