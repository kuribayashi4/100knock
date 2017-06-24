N_HEADS = int(input('N='))
with open('data/hightemp.txt', 'r') as f:
    head = "".join([f.readline() for line in range(N_HEADS)])
    print(head)