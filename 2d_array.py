# 行数
rows = 7
# 列数
cols = 5

# 10桁の文字列を左寄せ（左揃え）する
align_left = '%-10s'
# 右寄せ（右揃え）
align_right = '%10s'

# 2次元配列の宣言
arr = [[align_left %f'col{col}' for col in range(cols)] for row in range(rows)]

# 座標
arr[0][0] = align_left %'(0, 0)'
arr[3][2] = align_left %'(2, 3)'
arr[6][4] = align_left %'(4, 6)'

# 出力
for i in arr:
    for j in i:
        print(j, end=" ")
    print()


'''
行数（ぎょうすう）
列数（れつすう）
桁（けた）
左寄せ（ひだりよせ）＜＞右寄せ（みぎよせ）
左揃え（ひだりぞろえ）＜＞右揃え（みぎぞろえ）
左端（さたん）＜＞右端（うたん）
次元（じげん）
配列（はいれつ）
宣言（せんげん）
座標（ざひょう）
'''