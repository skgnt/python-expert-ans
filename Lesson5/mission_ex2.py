

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

#ここにinfo_pクラスを定義する。
class info_p(info):
    def periodic(self):
        self.age+=1
    def change_like(self,new):
        self.like_food=new


human=info_p("001",15,"りんご")
human.show()
human.periodic()
human.change_like("もも")
human.show()