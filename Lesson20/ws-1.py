
def my_pow(a,b):#def 関数名(引数):
    res=1   #計算結果を入れる変数を初期化
    for i in range(b):#for 変数 in range(回数):

        res=res*a#計算結果にaを掛ける
    # a=2
    # b=3の場合
    # for 1回目 res=res(1)*2
    # for 2回目 res=res(2)*2
    # for 3回目 res=res(4)*2

    return res #計算結果を返す

total=my_pow(2,3)
print(total)