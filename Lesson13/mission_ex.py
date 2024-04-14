#問題名:mission_ex
#概要:1~10のランダムな数字を当てるプログラム
import random

num =random.randint(1, 10)
print("ランダムに選ばれた数字を当ててください。")


while True:
    a = input("数字を入力してください。")
    #バグの原因:文字列と数値を比較している。
    #解決法:int()関数を使って、文字列を数値に変換する。
    if a == num:
        print("当たり！")
        break
    else:
        print("はずれ！")