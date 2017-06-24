from itertools import chain
from q45 import VerbFrame

class VerbFrame3(VerbFrame): 
    @classmethod
    def get_zyosi(cls, chunk, sentence):
        list_zyosi = []
        list_chunk = []
        for index_chunk in chunk.srcs:
            morphs = sentence[index_chunk].morphs
            for morph_i in range(len(morphs) - 1):
                if morphs[morph_i].pos1 == "サ変接続" and  morphs[morph_i + 1].base == "を":
                    list_zyosi.append("を")
                    list_chunk.append(morphs[morph_i].surface + "を")
        if list_zyosi == []:
            return ""
        else:
            list_zyosi.append(list_chunk)
            return list_zyosi
    
    @classmethod
    def make_data(cls, chunk, sentence):
        return ([cls.lget_verb(chunk), cls.get_zyosi(chunk, sentence)])

def main():
    with open("work/47.txt", "w") as f:
        for predicate in VerbFrame3.make_frame():
            cases = " ".join(list(chain.from_iterable(predicate[1])))
            if cases:
                f.write(predicate[0] + "\t" + cases + "\n")

if __name__ == "__main__":
    main()