import random

num_list = [random.randint(10) for i in range(10)]

for i in range(10):
    print(f"{i+1}つ目にランダムに選ばれた数字は{num_list[i]}です。")