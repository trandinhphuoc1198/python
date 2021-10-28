#Userが二つの数字を入力し、その範囲以内、7で割り切れるが、5の倍数ではないすべての数値を見つけるプログラムを作成します。 結果の数値は、コンマで区切られた1行の文字列として出力されます。
first = int(input("nhap so dau"))
last = int(input("nhap so cuoi"))
a = list(range(first,last))
n = 0
result = []
dem = len(a)

while n < dem  and int(a[n]) <= last:
    if a[n]%7 == 0 and not a[n]%5 == 0:
        result.insert(n,a[n])
    n += 1
print("ket qua la " +str(result))