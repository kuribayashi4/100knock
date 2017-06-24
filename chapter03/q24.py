import re
with open('work/UK.txt') as f:
    search_filenames = re.compile('(\[\[)?(?<=ファイル:|File:).+?\]\]')
    for line in f:
        filenames = search_filenames.finditer(line)
        if filenames:
            for filename in filenames:
                print(re.split('ファイル:|File:|\|',filename.group())[0])