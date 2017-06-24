with open('data/hightemp.txt', 'r') as f:
    data = [line.split() for line in f] #リストのリスト
    sort_col3 = sorted(data, reverse = True, key = lambda x: float(x[2]))
    print("\n".join(["\t".join(data) for data in sort_col3]))