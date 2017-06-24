import xml.etree.ElementTree as ET
tree = ET.parse('work/nlp.txt.xml')
root = tree.getroot()
for token in root.iter('token'):
    print("{}\t{}\t{}".format(token[0].text, token[1].text, token[4].text))