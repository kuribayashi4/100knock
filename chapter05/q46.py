from itertools import chain
from q45 import VerbFrame

class VerbFrame2(VerbFrame):    
    @classmethod
    def get_chunk(cls, chunk):
        list_chunk = []
        for morph in chunk.morphs:
            if morph.pos == "助詞": 
                list_chunk.append(str(chunk))
        return list_chunk
    
    @classmethod
    def make_data(cls, chunk, sentence):
        return ([cls.lget_verb(chunk), 
                 [cls.get_zyosi(sentence[index_srcs]) for index_srcs in chunk.srcs],
                    [cls.get_chunk(sentence[index_srcs]) for index_srcs in chunk.srcs]])

def main():
    with open("work/46.txt", "w") as f:
        for predicate in VerbFrame2.make_frame():
            cases = " ".join(list(chain.from_iterable(predicate[1])))
            chunks = " ".join(list(chain.from_iterable(predicate[2])))
            if cases: 
                f.write(predicate[0] + "\t" + cases + " " + chunks + "\n")

if __name__ == "__main__":
    main()