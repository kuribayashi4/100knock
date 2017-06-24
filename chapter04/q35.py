from q30 import neko
from itertools import groupby
connected_noun = set()
for sentence in neko:
    for is_noun, noun_block in groupby(sentence, lambda x: x['pos'] == "名詞"):
        if is_noun :
            nouns = list(noun_block)
            if len(nouns) > 1:
                connected_noun.add("".join(noun['surface'] for noun in nouns))
print(connected_noun)