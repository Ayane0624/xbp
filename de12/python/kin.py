while True:
    q1 = input('Q1　時間はいつですか？1　朝/2　昼/3　夕方/4　夜：')
    q2 = input('Q2　場所はどこですか？1　屋内/2　屋外：')
    q3 = input('Q3　あなたの今の感情はどんなものですか？1　楽しい/2　悲しい/3　イライラ：')
    q4 = input('Q4　今の状況はそんなものですか？1　/2　/3　：')
    if   q1 == '1' and q2 == '1' and q3 =='1' and q4 =='1':
        ans = '熱くて苦い'
    elif q1 == '2' and q2 == '1' and q3 =='1' and q4 =='1':
        ans = '熱くて甘い'
    elif q1 == '3' and q2 == '1' and q3 =='1' and q4 =='1':
        ans = '冷たくて苦い'
    elif q1 == '4' and q2 == '1' and q3 =='1' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '2' and q3 =='1' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '3' and q3 =='1' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '4' and q3 =='1' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '1' and q3 =='2' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '1' and q3 =='3' and q4 =='1':
        ans = '冷たくて甘い'
    elif q1 == '1' and q2 == '1' and q3 =='4' and q4 =='1':
        ans = '冷たくて甘い'
    else:
        print('A, あなたへのオススメはスパムです。')
        break

    print('A, 今のあなたへおすすめの曲は{}です。'.format(ans))
