import sys
N_HEADS = int(sys.argv[1])
with open('data/hightemp.txt', 'r') as f:
    head = "".join([f.readline() for line in range(N_HEADS)])
    print(head)