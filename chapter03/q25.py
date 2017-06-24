import re
import pprint
from collections import OrderedDict
def template():
    info = ""
    with open('work/UK.txt') as f:
        for line in f:
            if line == "}}\n":
                break
            else:
                info = info + line
        return info

basic_info_dict=OrderedDict()
match_info = re.compile("([^=]+) = (.+)",flags = re.S)
for line in template().split("\n|"):
    match_bi = match_info.match(line)
    if match_bi:
        basic_info_dict.update({match_bi.group(1):match_bi.group(2)})
pprint.pprint(basic_info_dict)