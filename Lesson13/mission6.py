#問題名:mission6
#概要:1から100までのランダムな数字を10個配列に格納し、それぞれの数字を表示するプログラム
import random


num_list = [random.randint(1, 10) for i in range(10)]
count=0
#エラー原因:num_listの要素が10個であるが、その範囲外を指定している。
#エラー内容:IndexError: list index out of range
#解決法:while文の条件を修正して、範囲外を指定しないようにする。
# while count<=10:
while count<10:
    print(f"{count+1}つ目にランダムに選ばれた数字は{num_list[count]}です。")
    count+=1

print(num_list)

    