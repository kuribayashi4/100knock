from graphviz import Digraph
import xml.etree.ElementTree as ET
tree = ET.parse('work/nlp.txt.xml')
root = tree.getroot()

def dependency_tree(i_sent):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    G.node("0", "ROOT")
    root = tree.getroot()
    for dep in root.findall(".//sentence[@id='{}']/dependencies[@type='collapsed-dependencies']/dep".format(i_sent)):
        G.node(dep[1].get('idx'), dep[1].text)
        G.edge(dep[0].get('idx'), dep[1].get('idx'))
    G.render("work/57")
    print(G)

dependency_tree(2)