while True:
    q1 = input('Q1　時間はいつですか？1　朝/2　昼/3　夕方/4　夜：')
    q2 = input('Q2　場所はどこですか？1　屋内/2　屋外：')
    q3 = input('Q3　あなたの今の感情はどんなものですか？1　楽しい/2　悲しい/3　イライラ：')
    if   q1 == '1' and q2 == '1' and q3 =='1':
        ans = '　'
    elif q1 == '1' and q2 == '1' and q3 =='2':
        ans = 'フィクション/sumika https://youtu.be/IKHGAuNaGuA '
    elif q1 == '1' and q2 == '1' and q3 =='3':
        ans = 'KiLLiNG ME/SiM https://youtu.be/vyUMYYc8lxU '
    elif q1 == '1' and q2 == '2' and q3 =='1':
        ans = 'ヒューマニティ！/サンボマスター https://youtu.be/SJKwDb3JWJM '
    elif q1 == '1' and q2 == '2' and q3 =='2':
        ans = '人として/SUPER BEAVER https://youtu.be/5cvXmuuC1GI '
    elif q1 == '1' and q2 == '2' and q3 =='3':
        ans = 'ENVY/coldrain https://youtu.be/2teepAfDrXI '
    elif q1 == '2' and q2 == '1' and q3 =='1':
        ans = 'GO!!!/FLOW https://youtu.be/zejYD43HyQo '
    elif q1 == '2' and q2 == '1' and q3 =='2':
        ans = '明日、また/[Alexandros] https://youtu.be/qVDgV2JQydk '
    elif q1 == '2' and q2 == '1' and q3 =='3':
        ans = 'Rave-up Tonight/Fear, and Loathing in Las Vegas https://youtu.be/BDFD2WopIjY '
    elif q1 == '2' and q2 == '2' and q3 =='1':
        ans = 'キラーチューン/東京事変　https://youtu.be/lC8la4l4RhQ '
    elif q1 == '2' and q2 == '2' and q3 =='2':
        ans = '　'
    elif q1 == '2' and q2 == '2' and q3 =='3':
        ans = '　'
    elif q1 == '3' and q2 == '1' and q3 =='1':
        ans = '　'
    elif q1 == '3' and q2 == '1' and q3 =='2':
        ans = '　'
    elif q1 == '3' and q2 == '1' and q3 =='3':
        ans = '　'
    elif q1 == '3' and q2 == '2' and q3 =='1':
        ans = '　'
    elif q1 == '3' and q2 == '2' and q3 =='2':
        ans = '　'
    elif q1 == '3' and q2 == '2' and q3 =='3':
        ans = '　'
    elif q1 == '4' and q2 == '1' and q3 =='1':
        ans = '　'
    elif q1 == '4' and q2 == '1' and q3 =='2':
        ans = '　'
    elif q1 == '4' and q2 == '1' and q3 =='3':
        ans = '　'
    elif q1 == '4' and q2 == '2' and q3 =='1':
        ans = '　'
    elif q1 == '4' and q2 == '2' and q3 =='2':
        ans = '　'
    elif q1 == '4' and q2 == '2' and q3 =='3':
        ans = '　'
    else:
        print('A, あなたへのオススメは判断不可です。')
        break

    print('A, 今のあなたへおすすめの曲は{}です。'.format(ans))
