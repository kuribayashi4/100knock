from itertools import groupby
from cytoolz import nth
file_path = 'work/neko.txt.cabocha'
class Morph:
    def __init__(self, surface, base, pos, pos1): 
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        
    def __str__(self):
        return "{}\t{}, {}, {}".format(self.surface, self.base, self.pos, self.pos1)

    @classmethod
    def sent2morph(cls, sent_block): #文をmorphオブジェクトのリストに
        sentence = []
        for line in sent_block:
            if not line.startswith("* "):
                details = line.rstrip().replace("\t", ",").split(",")
                sentence.append(Morph(details[0], details[7], details[1], details[2]))
        return sentence
    
def parse():
    with open(file_path, 'r') as f:
        for is_eos, sent_block in groupby(f, lambda x: x.strip() == "EOS"): #文単位に分ける
            if not is_eos:
                yield Morph.sent2morph(sent_block)    
                
def main():
    neko = parse()
    for morph in nth(3, neko):
        print(morph)
            
if __name__ == "__main__":
    main()