import re
with open('work/UK.txt', 'r') as f:
    for line in f:
        if re.match('\[\[Category:.*?\]\]',line):
            print(line.strip("\n"))