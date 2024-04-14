#問題名:mission4
#概要:
#何がエラーの原因かを考えて修正してみましょう。
num=int(input("数字を入力してください:"))
res=[]

#エラー原因:0で割り算をしている。
#エラー内容:ZeroDivisionError: division by zero
#解決法:0で割り算をしないようにするため、1から開始にする。(1からでなくとも正解)
# for i in range(10):
for i in range(1,10):
    
    res.append(num/i)

print(res)