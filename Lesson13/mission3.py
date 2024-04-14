#問題名:mission3
#概要:最初に10を代入したリストに1から100までのランダムな数字を10個追加して、表示するプログラム
import random

#エラー原因:10はint型であるが、int型にはappend()メソッドがない。
#エラー内容:AttributeError: 'int' object has no attribute 'append'
#解決法:rand_listをリスト型に変更する。
# rand_list=10
rand_list=[10]

for i in range(10):
    rand_list.append(random.randint(1,100))

print(rand_list)