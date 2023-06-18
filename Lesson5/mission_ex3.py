#改変しないで
class info:
    def __init__(self,id,age,like_food):
        self.id=id
        self.age=age
        self.like_food=like_food
    def show(self):
        print("-------------")
        print(f"ID:{self.id}")
        print(f"年齢:{self.age}")
        print(f"好きな食べ物:{self.like_food}")
#ここまで

#ここにinfo_aクラスを定義する。
class info_a(info):
    def __init__(self, id, age, like_food,birthday,country):
        super().__init__(id, age, like_food)
        self.birthday=birthday
        self.country=country
    def show(self):
        super().show()
        print(f"誕生日:{self.birthday}")
        print(f"出身:{self.country}")





#確認用
human=info_a("001",15,"りんご","1月1日","日本")
human.show()
