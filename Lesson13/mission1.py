#問題名:mission1
#概要:1から10までのランダムな数字を出力してください。
import random

num =random.randint(1, 10)
#エラー原因:数字と文字列を結合している。
#エラー内容:TypeError: can only concatenate str (not "int") to str
#解決法:str()関数を使って、数値を文字列に変換する。
#print("ランダムに当てられた数字は"+num+"です。")
print("ランダムに当てられた数字は"+str(num)+"です。")