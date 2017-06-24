from graphviz import Digraph
from q41 import parse
from cytoolz import nth

def make_tree(sentence):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    for chunk in sentence:
        surf_chunk = str(chunk)
        if surf_chunk: 
            G.node(str(chunk.index), surf_chunk)
            if chunk.dst != -1: 
                G.edge(str(chunk.index), str(chunk.dst))
    G.render('work/44')
    print(G)

def main():
    make_tree(nth(3, parse()))
    
if __name__ == "__main__":
    main()