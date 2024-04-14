import random


num_list = [random.randint(1, 10) for i in range(10)]
count=0
while count<=10:
    print(f"{count+1}つ目にランダムに選ばれた数字は{num_list[count]}です。")
    count+=1


    