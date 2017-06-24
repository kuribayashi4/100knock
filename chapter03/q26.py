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
        bi_value = match_bi.group(2)
        bi_value = re.sub(r"('{2,5})(.+?)\1", r'\2', bi_value)
        basic_info_dict.update({match_bi.group(1):bi_value})
pprint.pprint(basic_info_dict)