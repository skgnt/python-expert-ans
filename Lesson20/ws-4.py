# listの中身を全て足す関数
def list_sum(n):#def 関数名(引数):
    total = 0#計算結果を入れる変数を初期化

    for i in range(len(n)):#for 変数 in range(回数):
        total += n[i]#計算結果にnのi番目の要素を足す
    # n=[2,5]の場合
    # for 1回目 total=total(0)+n[0](2)
    # for 2回目 total=total(2)+n[1](5)
    return total #計算結果を返す
res=list_sum([1,2,5,6,7])
print(res)