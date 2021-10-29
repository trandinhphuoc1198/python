#Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
#与えられた数の階乗を計算できるプログラムを書く。 結果は、コンマで区切られた1行の文字列として出力されます。
#たとえば、指定された数が8の場合、出力は40320になります。
x = (int(input("nhap so")))
y=list(range(1,x,2))
for giai in y:
    x=x*giai
print(x)