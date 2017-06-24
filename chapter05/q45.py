from itertools import chain
from q41 import parse

class VerbFrame:
    @classmethod
    def lget_verb(cls, chunk):
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                return morph.base
        return False 
    
    @classmethod
    def get_zyosi(cls, chunk):
        list_zyosi = []
        for morph in chunk.morphs:
            if morph.pos == "助詞":
                list_zyosi.append(morph.base)
        return list_zyosi
    
    @classmethod
    def make_data(cls, chunk, sentence):
        return ([cls.lget_verb(chunk),[cls.get_zyosi(sentence[index_srcs]) 
                                       for index_srcs in chunk.srcs]])
    
    @classmethod
    def make_frame(cls):
        for sentence in parse():
            for chunk in sentence:
                if cls.lget_verb(chunk):
                    yield cls.make_data(chunk, sentence)
def main():
    with open("work/45.txt", "w") as f:
        for predicate in VerbFrame.make_frame():
            cases = " ".join(list(chain.from_iterable(predicate[1])))
            if cases:
                f.write(predicate[0] + "\t" + cases + "\n")

if __name__ == "__main__":
    main()