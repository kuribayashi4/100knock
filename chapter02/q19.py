from collections import Counter
with open('data/hightemp.txt', 'r') as f:
    data_col1 = [data.split()[0] for data in f]
    count_col1 = Counter(data_col1) 
    print("".join([str(cnt) + ' ' + word + '\n' for word, cnt in count_col1.most_common()]))