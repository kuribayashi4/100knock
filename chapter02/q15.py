import sys
def count_lines(file):
    return sum(1 for line in file)

N_TAILS = int(sys.argv[1])
with open('data/hightemp.txt', 'r') as f:
    LAST_NOT_DISP_LINE = count_lines(f) - N_TAILS 
    f.seek(0)
    for li, _ in enumerate(f, start=1):
        if li == LAST_NOT_DISP_LINE:
            break
    print("".join(f.readlines()))