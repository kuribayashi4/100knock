import xml.etree.ElementTree as ET
import sexpr
def parse():
    tree = ET.parse('work/nlp.txt.xml')
    root = tree.getroot()
    for s in root.findall(".//parse"):
        list_s = sexpr.str2sexpr(s.text)
        search_np(list_s)

def search_np(list_s):
    if len(list_s) == 1:
        search_np(list_s[0])
    elif list_s[0] == "NP":
        print_np(list_s)
        for element in list_s[1:]:
            search_np(element)
        print()
    elif isinstance(list_s[1], list):
        for element in list_s[1:]:
            search_np(element)
    return

def print_np(list_s):
    for element_np in list_s[1:]:
        if isinstance(element_np[1], str):
            print(element_np[1], end=" ")
        else:
            print_np(element_np)

parse()