from q48 import make_pathes_list
from itertools import combinations

def rule(path1, path2):
    for index_chunk1 in range(len(path1)):
        for index_chunk2 in range(len(path2)):
            if path1[index_chunk1] == path2[index_chunk2]:
                k = path1[index_chunk1] #文節k
                i_to_k = [str(path1[i_ch1]) if i_ch1 > 0 else path1[i_ch1].surface_q49("X")
                          for i_ch1 in range(index_chunk1)]
                j_to_k = [str(path2[i_ch2]) if i_ch2 > 0 else path2[i_ch2].surface_q49("Y")
                          for i_ch2 in range(index_chunk2)]
                return [i_to_k, j_to_k, k]
def main():
    pathes = make_pathes_list(5)
    pathes_q49 = [] #抽出されたパスのリスト
    for path_comb in combinations(pathes, 2):
        pathes_q49.append(rule(*path_comb))
    for path_q49 in pathes_q49:
        if isinstance(path_q49, type(None)): pass
        elif not(len(path_q49[0]) and len(path_q49[1])) :
            print(" -> ".join(path_q49[0]) + " -> ".join(path_q49[1]) + " -> " + path_q49[2].surface_q49("Y"))
        else:
            print("->".join(path_q49[0]) + " | " + " -> ".join(path_q49[1]) + " | " + str(path_q49[2]))

if __name__ =="__main__":
    main()