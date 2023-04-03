class character:
    def __init__(self, work, points):
        self.work = work
        self.points = points

    def info(self):
        print(self.work)
        print(self.points)


print("名前:HP(ヒットポイント)")
human1 = character("主人公", 150)
human1.info()

human2 = character("魔法つかい", 80)
human2.info()
