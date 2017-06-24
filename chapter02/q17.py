with open('data/hightemp.txt', 'r') as f:
    print(set(line.split()[0] for line in f))