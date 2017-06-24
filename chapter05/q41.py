from q40 import Morph
from itertools import groupby
from cytoolz import nth
file_path = 'work/neko.txt.cabocha'

class Chunk(Morph):
    def __init__(self): 
        self.morphs = []
        self.dst = -1
        self.srcs = []
        self.index = 0

    def details(self): #結果出力用
        return ("<chunk{}> 係り先:{}, 係り元:" 
                + " ".join(str(index) for index in self.srcs) + "\n" 
                + "\n".join(str(morph) for morph in self.morphs) + "\n").format(self.index, self.dst)

    def __str__(self): #文節の文字列を返す
        return ("".join(morph.surface for morph in self.morphs if morph.pos != "記号")).strip()
    
    def surface_q49(self, alphabet): #名詞をalphabetに置き換えて表示(q49で利用)
        chunk_surface = ""
        for index_morph in range(len(self.morphs)):
            if self.morphs[index_morph].pos != "記号":
                if self.morphs[index_morph].pos == "名詞":
                    chunk_surface = chunk_surface + alphabet
                else:
                    chunk_surface = chunk_surface + self.morphs[index_morph].surface
        return chunk_surface
                                                            
    @classmethod
    def _dependency(cls, sentence): #係り元の文節のindexを探す
        for chunk in sentence:
            if chunk.dst > -1:
                sentence[chunk.dst].srcs.append(chunk.index)
            
    @classmethod
    def sent2chunk(cls, sent_block): #文をchunkのリストに
        sentence = []
        for is_chunk, chunk_or_morphs in groupby(sent_block, lambda x: x.startswith("*")):
            if is_chunk:
                details = list(chunk_or_morphs)[0].lstrip("*").strip().split()
                chunk = Chunk()
                chunk.dst = int(details[1].rstrip("D"))
                chunk.index = int(details[0])
            if not is_chunk:
                chunk.morphs = Morph.sent2morph(chunk_or_morphs) #親のメソッドで形態素のリストに
                sentence.append(chunk)
        cls._dependency(sentence)
        return sentence

def parse():
    with open(file_path, 'r') as f:
        for is_eos, sent_block in groupby(f, lambda x: x.strip() == "EOS"): #文単位に分ける
            if not is_eos:
                yield Chunk.sent2chunk(sent_block)
def main():
    neko = parse()
    for chunk in nth(7, neko):
        print(chunk.details())
        
if __name__ == "__main__":
    main()