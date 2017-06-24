import re
with open('work/UK.txt') as f:
    regex_section = re.compile('(={2,})(.+?)(={2,})')
    for line in f:
        section = regex_section.match(line)
        if section:
            N_equal_left = section.group(1)
            if N_equal_left == section.group(3): #左右のイコールの数が一致していない時はセクションとみなさない
                print(section.group(2) + " " + str(len(N_equal_left)-1))