from itertools import islice
from cytoolz import nth
from q41 import parse

def depend():
    for sentence in parse():
        sent_depend = []
        for chunk in sentence:
            if str(chunk) and chunk.dst != -1:
                sent_depend.append(str(chunk) + "\t" + str(sentence[chunk.dst]))
        yield sent_depend 

def main():
    for sent_depend in islice(depend(),7,8):
        for dependency in sent_depend:
            print(dependency)
            
if __name__ == "__main__":
    main()