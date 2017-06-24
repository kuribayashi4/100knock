import sys
def div_list(data, N_DIV):
    N_LINES = len(data)
    start=0
    for i in range(int(N_DIV)):
        with open('work/split_{}.txt'.format(i), 'w') as f:
            n_elements = (N_LINES + i) // N_DIV #何行を１つの分割とするか
            f.write("".join(data[start:start+n_elements]))
            start = start + n_elements  

with open('data/hightemp.txt', 'r') as f:
    div_list(f.readlines(), sys.argv[1])