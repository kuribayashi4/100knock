from q41 import parse
from itertools import islice
from cytoolz import nth

def exist_noun(chunk):
    for morph in chunk.morphs:
        if morph.pos == "名詞":
            return True
        
def chunk_is_root(chunk):
    if chunk.dst == -1:
        return True

def noun_to_root(sentence):
    roots = []
    for chunk in sentence:
        to_root = []
        if exist_noun(chunk):
            while(not(chunk_is_root(chunk))):
                to_root.append(chunk)
                chunk = sentence[chunk.dst]
            to_root.append(chunk)
            roots.append(to_root)
            to_root=[]
    return roots

def make_pathes_list(line_index):
    neko = parse()
    pathes = [[chunk for chunk in chunk_list if len(chunk_list) > 1] for chunk_list in noun_to_root(nth(line_index, neko))]
    return pathes

def main():
    for path in make_pathes_list(5):
        print("->".join([str(chunk) for chunk in path]))
    
if __name__ == "__main__":
    main()