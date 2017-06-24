from itertools import islice
from q41 import parse

def is_pos(chunk, pos):
    for morph in chunk.morphs:
        if morph.pos == pos:
            return True
        
def depend():
    for sentence in parse():
        sent_depend = []
        for chunk in sentence:
            if all((str(chunk), chunk.dst != -1,
                    is_pos(chunk, "名詞"), is_pos(sentence[chunk.dst], "動詞"))):
                sent_depend.append(str(chunk) + "\t" + str(sentence[chunk.dst]))
        yield sent_depend 

def main():
    for sent_depend in islice(depend(),0,8):
        for dependency in sent_depend:
            print(dependency)

if __name__ ==  "__main__":
    main()