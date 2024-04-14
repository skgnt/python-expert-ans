#問題名:mission7
#概要:ランダムな整数のリストを作成し、その中の最大値を求めるプログラムを作成してください。
import random

#エラー原因:関数内でmaxを変更しようとしているが、その変数が関数内で定義されていない。
#エラー内容:UnboundLocalError: cannot access local variable 'max' where it is not associated with a value
#解決法:関数内でmaxを定義する。(グローバル宣言でも可)
def max_value(numbers):
    max=0
    for n in numbers:
        if n > max:
            max = n
    return max


#max=0


rand_list=[random.randint(1,100) for i in range(10)]
print("最大値は"+str(max_value(rand_list))+"です。")