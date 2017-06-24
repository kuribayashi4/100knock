with open('data/hightemp.txt', 'r') as f, open('work/col1.txt', 'w') as f1, open('work/col2.txt', 'w') as f2:
    for line in f:
        col = line.split()
        f1.write(col[0] + '\n') #1列目のデータをcol1.txtに書き込み
        f2.write(col[1] + '\n') #2列目のデータをcol2.txtに書き込み