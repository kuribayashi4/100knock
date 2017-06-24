import re
with open('work/UK.txt', 'r') as f:
    match_category = re.compile('\[\[Category:.*?\]\]')
    print("\n".join(re.split(r'[]:|]', line)[1] for line in f if match_category.match(line)))