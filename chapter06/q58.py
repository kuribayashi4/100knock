import xml.etree.ElementTree as ET
def dep_nd():
    tree = ET.parse('work/nlp.txt.xml')
    root = tree.getroot()
    dep_n = [(dep_nsubj[0], dep_nsubj[1]) 
     for dep_nsubj in root.findall(".//dependencies[@type='collapsed-dependencies']/dep[@type='nsubj']")]
    dep_d = [(dep_nsubj[0], dep_nsubj[1]) 
     for dep_nsubj in root.findall(".//dependencies[@type='collapsed-dependencies']/dep[@type='dobj']")]
    make_tuple(dep_n, dep_d)

def make_tuple(dep_n, dep_d):
    for n in dep_n:
        for s in dep_d:
            if n[0].get('id') == s[0].get('id'):
                print(n[1].text, n[0].text, s[1].text)

dep_nd()   