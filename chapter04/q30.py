from itertools import groupby
from pprint import pprint
neko = []
with open("work/neko.txt.mecab", "r") as f:
    for is_eos, sent_block in groupby(f, key=lambda x: x.strip() == "EOS"):
        if not is_eos:
            sentence = []
            for line in sent_block:
                details = line.rstrip().replace("\t", ",").split(",")
                morph = {
                    "surface": details[0],
                    "base": details[7],
                    "pos": details[1],
                    "pos1": details[2]
                }
                sentence.append(morph)
            neko.append(sentence)