name="aaa"
tall=153
weight=41
# 上下名前一致で使える
print(name, "さんは身長", tall, "cmで体重は",weight, "キロですね。")

name="aaa"
waist=84
age=70

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

a=1
if age > 65:
    print(name,"さんは高齢者です")
else:
    print(name,"さんは高齢者ではありません")
    # ,で区切る