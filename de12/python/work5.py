for i in range(1,4): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！

    name=input("名前を教えて下さい")
    tall=float(input("身長を教えて下さい"))
    weight=float(input("体重を教えて下さい"))
    # 上下名前一致で使える
    print(name, "さんは身長", tall, "cmで体重は",weight, "キロですね。")

    name=input("名前を教えて下さい")
    waist=float(input("腹囲を教えて下さい"))
    age=int(input("年齢を教えて下さい"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    a=1
    if age > 65:
        print(name,"さんは高齢者です")
    else:
        print(name,"さんは高齢者ではありません")
        # ,で区切る

